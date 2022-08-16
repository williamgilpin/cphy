#!/usr/bin/python
import numpy as np



from sklearn.base import BaseEstimator, TransformerMixin

# We are going to use class inheritance to define our object. The two base classes from
# scikit-learn represent placeholder objects for working with datasets. They include 
# many generic methods, like fetching parameters, getting the data shape, etc.
# 
# By inheriting from these classes, we ensure that our object will have access to these
# functions, even though we don't have to define them ourselves
class PrincipalComponents(BaseEstimator, TransformerMixin):
    """
    A class for performing principal component analysis on a dataset.
    """

    def __init__(self, random_state=None):
        self.random_state = random_state
        self.components_ = None
        self.singular_values_ = None

    def fit(self, X):
        """
        Fit the PCA model to the data X. Store the eigenvectors in the attribute
        self.components_ and the eigenvalues in the attribute self.singular_values_

        Args:
            X (np.ndarray): A 2D array of shape (n_samples, n_features) containing the
                data to be fit.
        
        Returns:
            self (PrincipalComponents): The fitted object.
        """

        ########## YOUR CODE HERE ##########
        #
        # # YOUR CODE HERE
        # # Hint: Keep track of whether you should be multiplying by a matrix or
        # # its transpose.
        #
        ########## YOUR CODE HERE ##########
        # raise NotImplementedError()
        
        Xc = X - np.mean(X, axis=0)

        cov = Xc.T.dot(Xc) / Xc.shape[0]
        # cov = np.cov(Xc, rowvar=False) # Alternatively, using the numpy built-in
        S, V = np.linalg.eigh(cov)
        V = V.T
        sort_inds = np.argsort(S)[::-1] # sort eigenvalues in descending order
        S, V = S[sort_inds], V[sort_inds]

        # Alternative, using singular value decomposition
        # U, S, V = np.linalg.svd(Xc, full_matrices=False)
        # S = S**2 / Xc.shape[0]

        self.components_ = V
        self.singular_values_ = S

        return self

    def transform(self, X):
        """
        Transform the data X into the new basis using the PCA components
        """
        # # YOUR CODE HERE
        # raise NotImplementedError()

        Xc = X - np.mean(X, axis=0)
        return Xc.dot(self.components_.T)

    def inverse_transform(self, X):
        """
        Transform from principal components space back to the original space
        """
        # # YOUR CODE HERE
        # raise NotImplementedError()
        return X.dot(self.components_) + np.mean(X, axis=0)






