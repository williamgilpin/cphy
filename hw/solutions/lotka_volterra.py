from scipy.integrate import solve_ivp

class LotkaVolterra:
    """
    An implementation of the Lotka-Volterra model

    Parameters:
        n (int): number of species
        sigma (float): the scale of the randomly-sampled elements, Defaults to 1.0
        d (float): the density-limitation strength. Defaults to 10.0

    """

    def __init__(self, N, sigma=1.0, d=12.5, random_state=None):
        ################################################################################
        #
        #
        #  YOUR CODE HERE
        #  The instructor solution is ten lines and uses np.random.normal() and 
        #  np.random.seed()
        #
        #
        ################################################################################
        # raise NotImplementedError("Implement this method")

        self.N = N
        self.sigma = sigma
        self.random_state = random_state
        np.random.seed(self.random_state)
        ## Create a hollow random matrix
        self.r = np.random.normal(size=(self.N,), scale=self.sigma)
        self.A = np.random.normal(size=(self.N, self.N), scale=self.sigma)
        self.A = self.A - np.diag(self.A)
        self.d = d


    def rhs(self, t, n):
        """
        Given a time and a state vector, return the right-hand side of the Lotka-Volterra equations
        """
        ################################################################################
        #
        #
        #  YOUR CODE HERE
        #  The instructor solution is one line
        #
        #
        ################################################################################
        # raise NotImplementedError("Implement this method")

        return n * (self.r + np.dot(self.A, n) - self.d * n)
    

class LotkaVolterraWithJacobian(LotkaVolterra):
    """
    A subclass of the Lotka-Volterra model that adds a Jacobian functions
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def jacobian(self, t, n):
        """
        Given a time and a state vector, return the Jacobian of the Lotka-Volterra equations
        """
        ################################################################################
        #
        #
        #  YOUR CODE HERE.
        #
        #
        ################################################################################
        A2 = self.A - self.d * np.eye(self.N)
        return np.diag(self.r + np.dot(A2, n)) + A2 * n[:, None]