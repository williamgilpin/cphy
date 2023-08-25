import numpy as np
import matplotlib.pyplot as plt

class RandomGaussianLandscape:
    """
    Create a random two-dimensional loss landscape with multiple circular gaussian wells

    Args:
        d (int): the dimensionality of the landscape
        n_wells (int): the number of wells to include in the landscape
        random_state (int): the random seed to use for generating the landscape
    """

    def __init__(self, d=2, n_wells=3, random_state=None):
        
        self.random_state = random_state
        np.random.seed(random_state)
        self.coeffs = np.random.random(n_wells)
        self.coeffs /= np.sum(self.coeffs)
        self.locs = np.random.randn(n_wells, d)
        self.widths = np.random.rand(n_wells)[None, :]

    def _gaussian_well(self, X, width=1):
        return -np.exp(-np.sum((X / width) ** 2, axis=1))

    def _grad_gaussian_well(self, X, width=1):
        return -2 * X / (width ** 2) * self._gaussian_well(X, width)[:, None, :]

    def loss(self, X):
        # X shape before summation is (n_batch, n_dim)
        # Arg shape before summation is (n_batch, n_wells)
        # print(self._gaussian_well(X[..., None] - self.locs.T[None, :], self.widths).shape)
        return np.einsum(
            '...i,i->...', 
            self._gaussian_well(X[..., None] - self.locs.T[None, :], self.widths), 
            self.coeffs
        )

    def grad(self, X):
        # Arg shape before summation is (n_batch, n_dim, n_wells)
        return np.einsum(
            '...i,i->...', 
            self._grad_gaussian_well(X[..., None] - self.locs.T[None, :], self.widths), 
            self.coeffs
        )
    
    def plot(self, ax=None, plot_bounds=[[-3, 3],[-3, 3]], n_mesh=100, **kwargs):
        """
        Plot the loss landscape

        Args:
            ax (matplotlib.axes.Axes): the axes on which to plot the landscape
            plot_bounds (list): the bounds of the plot
            n_mesh (int): the number of points to use in each dimension
            **kwargs: keyword arguments to pass to the scatter plot

        Returns:
            matplotlib.axes.Axes: the axes on which the landscape was plotted 
        """
        x = np.linspace(*plot_bounds[0], n_mesh)
        y = np.linspace(*plot_bounds[1], n_mesh)
        xx, yy = np.meshgrid(x, y)
        X = np.array([xx.ravel(), yy.ravel()]).T
        Z = self.loss(X) # same as loss.loss(X) because class is callable
        if ax is None:
            plt.figure(figsize=(8, 8))
            ax = plt.gca()
        plt.scatter(X[:, 0], X[:, 1], c=Z, **kwargs)
        plt.xlim(*plot_bounds[0])
        plt.ylim(*plot_bounds[1])
        return ax

    def __call__(self, X):
        return self.loss(X)