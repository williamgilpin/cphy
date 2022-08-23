#!/usr/bin/python
import numpy as np


import warnings
class SpectralDecompositionPowerMethod:
    """
    Store the output vector in the object attribute self.components_ and the 
    associated eigenvalue in the object attribute self.singular_values_ 
    
    Why this code structure and attribute names? We are using the convention used by 
    the popular scikit-learn machine learning library:
    https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

    Parameters
        max_iter (int): maximum number of iterations to for the calculation
        tolerance (float): fractional change in solution to stop iteration early
        gamma (float): momentum parameter for the power method
        random_state (int): random seed for reproducibility
        store_intermediate_results (bool): whether to store the intermediate results as
            the power method iterates
        stored_eigenvalues (list): If store_intermediate_results is active, a list of 
            eigenvalues at each iteration
        stored_eigenvectors (list): If store_intermediate_results is active, a list of
            eigenvectors at each iteration
    
    """
    def __init__(self, 
        max_iter=1000, 
        tolerance=1e-5, 
        gamma=0.0,
        random_state=None, 
        store_intermediate_results=False
    ):
        ########## YOUR CODE HERE ##########
        #
        # YOUR CODE HERE
        #
        ########## YOUR CODE HERE ##########
        # raise NotImplementedError()

        self.max_iter = max_iter
        self.tolerance = tolerance
        self.gamma = gamma
        self.random_state = random_state

        # Placeholders for the results of the calculation
        self.singular_values_ = None
        self.components_ = None
        
        self.store_intermediate_results = store_intermediate_results
        if self.store_intermediate_results:
            self.stored_eigenvalues = list()
            self.stored_eigenvectors = list()
    
    def fit(self, A):
        """
        Perform the power method with random initialization, and optionally store
        intermediate estimates of the eigenvalue and eigenvectors at each iteration.
        You can add an early stopping criterion based on the tolerance parameter.
        """
        ########## YOUR CODE HERE ##########
        #
        # YOUR CODE HERE
        # Hint: keep track of your normalization factors, and watch out for passing
        # arrays by value vs. by reference. This method should return self
        #
        ########## YOUR CODE HERE ##########
        # raise NotImplementedError()

        n = A.shape[0]
        np.random.seed(self.random_state)
        vec = np.random.random(n)
        vec = vec / np.linalg.norm(vec)

        if self.store_intermediate_results:
            self.stored_eigenvalues.append(1)
            self.stored_eigenvectors.append(vec)
        for i in range(self.max_iter):

            prev = np.copy(vec)
            vec = A.dot(vec)
            eig_val = np.linalg.norm(vec)
            vec = vec / eig_val

            vec = self.gamma * prev + (1 - self.gamma) * vec

            ## An even better heuristic: we update gamma based on the error signal
            # vec = (1 - err) * prev + err * vec
            # err = np.sqrt((vec - prev)**2 / prev**2)

            if self.store_intermediate_results:
                self.stored_eigenvalues.append(eig_val)
                self.stored_eigenvectors.append(vec)

            if np.mean(np.sqrt((vec - prev)**2 / prev**2)) < self.tolerance:
                warnings.warn(f"Power method converged before {self.max_iter} iterations")
                break
        
        if self.store_intermediate_results:
            self.stored_eigenvalues = np.array(self.stored_eigenvalues)
            self.stored_eigenvectors = np.array(self.stored_eigenvectors)
        
        self.singular_values_ = eig_val
        self.components_ = vec





