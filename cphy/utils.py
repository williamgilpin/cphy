import numpy as np

from sklearn.model_selection import train_test_split


def radial_profile(data, center=(0,0)):
    """
    Calculate the radial profile of a square array
    """
    y, x = np.indices((data.shape))
    r = np.sqrt((x-center[0])**2+(y-center[1])**2)
    ind = np.argsort(r.flat)
    sr = r.flat[ind]
    sim = data.flat[ind]
    ri = sr.astype(np.int32)

    deltar = ri[1:] - ri[:-1]
    rind = np.where(deltar)[0]
    nr = rind[1:] - rind[:-1]
    csim = np.cumsum(sim, dtype=np.float64)
    tbin = csim[rind[1:]] - csim[rind[:-1]]
    rad_prof = tbin/nr
    return rad_prof

def radial_psd(a):
    half = len(a) // 2
    psd = np.abs(np.fft.fft2(a))
    
    p1 = psd[:half, :half]
    p2 = np.flipud(psd[-half:, :half])
    p3 = np.fliplr(np.flipud(psd[-half:, -half:]))
    p4 = np.fliplr(psd[:half, -half:])
    
    p_ave = np.mean(np.dstack([p1, p2, p3, p4]), axis=-1)
    return radial_profile(p_ave)[:half]

class ReynoldsDataset:
    """
    Class to load the Reynolds number classification dataset
    
    Parameters:
        downsample (int): Factor by which to downsample the dataset
        split (float): Fraction of data to use for testing
        fourier_features (bool): Whether to use Fourier features instead of real space
    """

    def __init__(self, downsample=1, split=0.2, fourier_features=True):

        all_vorticity_fields = list()
        all_reynolds_numbers = list()

        # Load simulations for different Reynolds numbers
        re_vals = [300, 600, 900, 1200]
        for re_val in re_vals:

            # Load the two-dimensional velocity field data. Data is stored in a 4D numpy array,
            # where the first dimension is the time index, the second and third dimensions are the
            # x and y coordinates, and the fourth dimension is the velocity components (ux or uv).
            vfield = np.load(
                f"../resources/von_karman_street/vortex_street_velocities_Re_{re_val}_largefile.npz", 
                allow_pickle=True
            )

            # Calculate the vorticity, which is the curl of the velocity field
            vort_field = np.diff(vfield, axis=1)[..., :-1, 1] + np.diff(vfield, axis=2)[:, :-1, :, 0]

            # Take wake field only
            vort_field = vort_field[::6, -127:, :]
            
            if fourier_features:
                # Calculate the 2D Fourier coefficients
                vort_field = np.array([np.log(radial_psd(item))[:100] for item in vort_field])
            else:
                # downsample the dataset
                vort_field = vort_field[:, ::downsample, ::downsample]

            all_vorticity_fields.append(vort_field)
            all_reynolds_numbers.extend(re_val * np.ones(vort_field.shape[0]))

        self.data_shape = vort_field[0].shape

        all_vorticity_fields = np.vstack(all_vorticity_fields)
        all_reynolds_numbers = np.array(all_reynolds_numbers)

        X = np.reshape(all_vorticity_fields, (all_vorticity_fields.shape[0], -1))
        y = all_reynolds_numbers

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.X = np.vstack([X_train, X_test])
        self.y = np.hstack([y_train, y_test])

    def reshape(self, X):
        if len(X.shape) == 1:
            return X.reshape(self.data_shape)
        elif len(X.shape) == 2:
            return np.reshape(X, (X.shape[0], 127, 127))
        else:
            raise ValueError("X must be a 1D or 2D array")
    
    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]
