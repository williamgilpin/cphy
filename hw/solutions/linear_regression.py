#!/usr/bin/python
import numpy as np
import warnings


class BaseRegressor:
    """
    A base class for regression models.
    """
    def __init__(self):
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        """
        Fits the model to the data.
        """
        raise NotImplementedError("Subclasses must implement this method")

    def predict(self, X):
        return X @ self.weights + self.bias

    def score(self, X, y):
        """
        Returns the mean squared error of the model.
        """
        return np.mean((self.predict(X) - y)**2)




class LinearRegressor(BaseRegressor):
    """
    A linear regression model is a linear function of the form:
    y = w0 + w1 * x1 + w2 * x2 + ... + wn * xn

    The weights are the coefficients of the linear function.
    The bias is the constant term w0 of the linear function.

    Attributes:
        method: str, optional. The method to use for fitting the model.
        regularization: str, optional. The type of regularization to use.
    """
    
    def __init__(self, method="global", regularization="ridge", regstrength=0.1, **kwargs):
        super().__init__(**kwargs)
        self.method = method
        self.regularization = regularization
        self.regstrength = regstrength

    # functions that begin with underscores are private, by convention.
    # Technically we could access them from outside the class, but we should
    # not do that because they can be changed or removed at any time.
    def _fit_global(self, X, y):
        """
        Fits the model using the global least squares method.
        """
        ############################################################
        #
        #
        # YOUR CODE HERE
        #
        #
        ############################################################
        #raise NotImplementedError
        if self.regularization is None:
            self.weights = np.linalg.inv(X.T @ X) @ X.T @ y
        elif self.regularization == "ridge":
            self.weights = np.linalg.inv(X.T @ X + np.eye(X.shape[1]) * self.regstrength) @ X.T @ y
        else:
            warnings.warn("Unknown regularization method, defaulting to None")
            self.weights = np.linalg.inv(X.T @ X) @ X.T @ y
        self.bias = np.mean(y - X @ self.weights)
        return self.weights, self.bias

    def _fit_iterative(self, X, y, learning_rate=0.01):
        """
        Fit the model using gradient descent.
        """
        ############################################################
        #
        #
        # YOUR CODE HERE
        #
        #
        ############################################################
        #raise NotImplementedError
        self.weights = np.zeros((X.shape[1], X.shape[1]))
        self.bias = np.mean(y)
        for i in range(X.shape[0]):
            self.weights += learning_rate * (y[i] - X[i] @ self.weights - self.bias) * X[i] - self.regstrength * self.weights
        self.weights /= X.shape[0]
        return self.weights, self.bias

    def fit(self, X, y):
        """
        Fits the model to the data. The method used is determined by the
        `method` attribute.
        """
        ############################################################
        #
        #
        # YOUR CODE HERE. If you implement the _fit_iterative method, be sure to include
        # the logic to choose between the global and iterative methods.
        #
        #
        ############################################################
        #raise NotImplementedError
        if self.method == "global":
            out = self._fit_global(X, y)
        elif self.method == "iterative":
            out = self._fit_iterative(X, y)
        else:
            out = self._fit_global(X, y)
        return out

def featurize_flowfield(field):
    """
    Compute features of a 2D spatial field. These features are chosen based on the 
    intuition that the input field is a 2D spatial field with time translation 
    invariance.

    The output is an augmented feature along the last axis of the input field.

    Args:
        field (np.ndarray): A 3D array of shape (batch, nx, ny) containing the flow field

    Returns:
        field_features (np.ndarray): A 3D array of shape (batch, nx, ny, M) containing 
            the computed features stacked along the last axis
    """
    ############################################################################
    #
    #
    # YOUR CODE HERE
    # Hint: I used concatenate to combine the features together. You have some choice of
    # which features to include, but make sure that your features are computed 
    # separately for each batch element
    # My implementation is vectorized along the first (batch) axis
    #
    ############################################################################
    # raise NotImplementedError

    ## Compute the Fourier features
    field_fft = np.fft.fft2(field)
    field_fft = np.fft.fftshift(field_fft)
    field_fft_abs = np.log(np.abs(field_fft) + 1e-8)[..., None]
    field_fft_phase = np.angle(field_fft)[..., None]

    ## Compute the spatial gradients along x and y
    field_grad = np.gradient(field, axis=(-2, -1))
    field_grad = np.stack(field_grad, axis=-1)

    ## Compute the spatial Laplacian
    field_lap = np.stack(np.gradient(field_grad, axis=(-2, -1)), axis=-1)
    field_lap = np.sum(field_lap, axis=-1)

    field = field[..., None]
    field_features = np.concatenate(
        [field, field_grad, field_lap, field_fft_phase, field_fft_abs], 
        axis=-1
    )
    return field_features