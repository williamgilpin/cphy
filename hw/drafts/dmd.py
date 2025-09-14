import numpy as np
from scipy.linalg import svd, eig, pinv
from sklearn.base import BaseEstimator, TransformerMixin

import numpy as np
from scipy.linalg import svd, eig, pinv
from sklearn.base import BaseEstimator, TransformerMixin

class DMD(BaseEstimator, TransformerMixin):
    """
    Dynamic Mode Decomposition transformer.

    Parameters:
        n_components (int or None): Number of DMD modes to retain. If None, keep all.
        lag (int): Lag time for the DMD.

    Attributes:
        modes_ (ndarray, shape (n_features, r)): DMD modes Φ.
        eigenvalues_ (ndarray, shape (r,)): DMD eigenvalues λ.
        n_modes_ (int): Number of modes retained.
    """
    def __init__(self, n_components=None, lag=1):
        self.n_components = n_components
        self.lag = lag

    def fit(self, X, y=None):
        X = np.asarray(X)
        N, M = X.shape

        # build snapshot matrices
        X1 = X[:-self.lag].T  # shape (M, N-1)
        X2 = X[self.lag:].T   # shape (M, N-1)

        # truncated SVD of X1
        U, s, Vh = svd(X1, full_matrices=False)
        r = s.size if self.n_components is None else min(self.n_components, s.size)
        U_r = U[:, :r]
        S_r = np.diag(s[:r])
        V_r = Vh[:r, :].T

        # reduced linear operator
        A_tilde = U_r.T @ X2 @ V_r @ np.linalg.inv(S_r)

        # correct eigen-decomposition: values, vectors = eig(A_tilde)
        eigvals, eigvecs = eig(A_tilde)
        # Phi = X2 @ V_r @ np.linalg.inv(S_r) @ eigvecs
        Phi = U_r @ eigvecs

        sort_inds = np.argsort(np.abs(eigvals))[::-1]
        self.modes_       = Phi[:, sort_inds]
        self.eigenvalues_ = eigvals[sort_inds]
        self.n_modes_     = r
        return self


    def transform(self, X):
        X = np.asarray(X)
        coeffs = pinv(self.modes_) @ X.T
        return coeffs.T

    def fit_transform(self, X, y=None):
        return self.fit(X).transform(X)


# X is a dataset of shape (n_timesteps, )

dmd = DMD(n_components=20, lag=25)
dmd.fit(X)
X_dmd = dmd.transform(X)


plt.figure(figsize=(5, 5))
plt.plot(np.abs(dmd.eigenvalues_), '.', markersize=5)
plt.xlabel("Eigenvalue Rank")
plt.ylabel("Eigenvalue magnitude")

## Plot the modes on the unit circle to identify oscillations vs growth
plt.figure(figsize=(5, 5))
plt.plot(
    np.cos(np.linspace(0, 2*np.pi, 100)), np.sin(np.linspace(0, 2*np.pi, 100)), 
    '--', color='black'
)
plt.plot(np.real(dmd.eigenvalues_), np.imag(dmd.eigenvalues_), '.', markersize=5)
plt.plot(np.real(dmd.eigenvalues_), np.imag(dmd.eigenvalues_), 'x', markersize=20)
## Plot a circle of unit radius
for i, (x_i, y_i) in enumerate(zip(np.real(dmd.eigenvalues_), np.imag(dmd.eigenvalues_))):
    plt.text(x_i, y_i, str(i), fontsize=14, ha='right')



modes = dmd.modes_.reshape(vort_field.shape[1], vort_field.shape[2], -1)
plt.figure(figsize=(20, 10))
for i in range(8):
    plt.subplot(1, 8, i+1)
    vscale = np.percentile(np.abs(modes[:, :, i]), 99)
    plt.imshow(np.real(modes[:, :, i]), cmap="RdBu", vmin=-vscale, vmax=vscale)
    plt.title("Real(Mode {})".format(i))

plt.figure(figsize=(20, 10))
for i in range(8):
    plt.subplot(1, 8, i+1)
    vscale = np.percentile(np.abs(modes[:, :, i]), 99)
    plt.imshow(np.imag(modes[:, :, i]), cmap="RdBu", vmin=-vscale, vmax=vscale)
    plt.title("Imag(Mode {})".format(i))

## Plot the movie projected onto the principal components
plt.figure(figsize=(20, 10))
for i in range(8):
    plt.subplot(8, 1, i+1)
    plt.plot(X_dmd[:, i])
    plt.ylabel("DMD Mode {} Amp".format(i+1))
plt.xlabel("Time")

## Plot the time series against each other
plt.figure()
ax = plt.axes(projection='3d')
ax.plot(X_dmd[:, 0], X_dmd[:, 1], X_dmd[:, 2])