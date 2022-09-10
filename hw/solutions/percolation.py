#!/usr/bin/python
import numpy as np

class PercolationSimulation:
    """
    A simulation of a 2D directed percolation problem. Given a 2D lattice, blocked sites
    are denoted by 0s, and open sites are denoted by 1s. During a simulation, water is
    poured into the top of the grid, and allowed to percolate to the bottom. If water
    fills a lattice site, it is marked with a 2 in the grid. Water only reaches a site
    if it reaches an open site directly above, or to the immediate left or right 
    of an open site.

    I've included the API for my solution below. You can use this as a starting point, 
    or you can re-factor the code to your own style. Your final solution must have a 
    method called percolate that creates a random lattice and runs a percolation 
    simulation and
    1. returns True if the system percolates
    2. stores the original lattice in self.grid
    3. stores the water filled lattice in self.grid_filled

    + For simplicity, use the first dimension of the array as the percolation direction
    + For boundary conditions, assume that any site out of bounds is a 1 (occupied)
    + You should use numpy for this problem, although it is possible to use lists 



    Attributes:
        grid (np.array): the original lattice of blocked (0) and open (1) sites
        grid_filled (np.array): the lattice after water has been poured in
        n (int): number of rows and columns in the lattice
        p (float): probability of a site being blocked in the randomly-sampled lattice
            random_state (int): random seed for the random number generator
        random_state (int): random seed for numpy's random number generator. Used to 
            ensure reproducibility across random simulations. The default value of None
            will use the current state of the random number generator without resetting
            it.
    """

    def __init__(self, n=100, p=0.5, grid=None, random_state=None):
        """
        Initialize a PercolationSimulation object.

        Args:
            n (int): number of rows and columns in the lattice
            p (float): probability of a site being blocked in the randomly-sampled lattice
            random_state (int): random seed for numpy's random number generator. Used to
                ensure reproducibility across random simulations. The default value of None
                will use the current state of the random number generator without resetting
                it.
        """

        self.random_state = random_state # the random seed

        # Initialize a random grid if one is not provided. Otherwise, use the provided
        # grid.
        if grid is None:
            self.n = n
            self.p = p
            self.grid = np.zeros((n, n))
            self._initialize_grid()
        else:
            assert len(np.unique(np.ravel(grid))) <= 2, "Grid must only contain 0s and 1s"
            self.grid = grid.astype(int)
            # override numbers if grid is provided
            self.n = grid.shape[0]
            self.p = 1 - np.mean(grid)

        # The filled grid used in the percolation calculation. Initialize to the original
        # grid. We technically don't need to copy the original grid if we want to save
        # memory, but it makes the code easier to debug if this is a separate variable 
        # from self.grid.
        self.grid_filled = np.copy(self.grid)

    def _initialize_grid(self):
        """
        Sample a random lattice for the percolation simulation. This method should
        write new values to the self.grid and self.grid_filled attributes. Make sure
        to set the random seed inside this method.

        This is a helper function for the percolation algorithm, and so we denote it 
        with an underscore in order to indicate that it is not a public method (it is 
        used internally by the class, but end users should not call it). In other 
        languages like Java, private methods are not accessible outside the class, but
        in Python, they are accessible but access is discouraged by convention.

        Private methods are useful for functions that are necessary to support the 
        public methods (here, our percolate() method), but which we expect we might need
        to alter in the future. If we released our code as a library, others might 
        build software that accesses percolate(), and so we should not alter the 
        input/outputs because it's a public method
        """
        ###############################################################################

        ####### YOUR CODE HERE  ####### 
        # Hint: my solution is 3 lines of code in numpy

        ###############################################################################
        np.random.seed(self.random_state)
        self.grid = np.random.choice([1, 0], size=(self.n, self.n), p=[1 - self.p, self.p])
        self.grid_filled = np.copy(self.grid)
        

    def _flow_recursive(self, i, j):
        """
        Only used if we opt for a recursive solution.

        The recursive portion of the flow simulation. Notice how grid and grid_filled
        are used to keep track of the global state, even as our recursive calls nest
        deeper and deeper
        """

        ####### YOUR CODE HERE  #######################################################
        # Remember to check the von Neumann neighborhood of the current site. There should
        # be 4 recursive calls in total, and 4 base cases
        ###############################################################################

        # Base cases return None
        if i < 0 or i >= self.n:
            return None
        if j < 0 or j >= self.n:
            return None
        # skip blocked sites
        if self.grid[i, j] == 0:
            return None
        # skip already full sites
        if self.grid_filled[i, j] == 2:
            return None

        self.grid_filled[i, j] = 2

        self._flow_recursive(i + 1, j)
        self._flow_recursive(i, j + 1)
        self._flow_recursive(i, j - 1)
        self._flow_recursive(i - 1, j)

    ## RECURSIVE
    def _flow(self):
        """
        Run a percolation simulation using recursion

        This method writes to the grid and grid_filled attributes, but it does not
        return anything. In other languages like Java or C, this method would return
        void
        """

        ####### YOUR CODE HERE  ####### 
        # Hints my non-recursive solution contains one row-wise for loop, which contains 
        # several loops over individual lattice sites. You might need to visit each lattice 
        # site more than once per row. In my implementation, split the logic of checking
        # the von neumann neighborhood into a separate method _poll_neighbors, which
        # returns a boolean indicating whether a neighbor is filled
        #
        # My recursive solution calls a second function, _flow_recursive, which takes 
        # two lattice indices as arguments
        ###############################################################################

        for i in range(self.n):
            self._flow_recursive(0, i)


    def _poll_neighbors(self, i, j):
        """
        Check whether there is a filled site adjacent to a site at coordinates i, j in 
        self.grid_filled. Respects boundary conditions.
        """
        
        ####### YOUR CODE HERE  #######################################################
        # Hint: my solution is 4 lines of code in numpy, but you may get different 
        # results depending on how you enforce the boundary conditions in your solution.
        # Not needed for the recursive solution
        ###############################################################################
       
        # I enforce boundary conditions using max/min, but you can also manually check
        # Cases with if/else, or pad a series of zeros around the lattice to enforce
        # occupied sites at the edges.
        top = self.grid_filled[max(i - 1, 0), j] == 2
        right = self.grid_filled[max(i, 0), min(j + 1, self.n - 1)] == 2
        left = self.grid_filled[max(i, 0), max(j - 1, 0)] == 2
        bottom = self.grid_filled[min(i + 1, self.n - 1), j] == 2

        return any([top, left, right, bottom])

    ## NON-RECURSIVE
    def _flow(self):
        """
        Run a directed percolation simulation without recursion

        This method writes to the grid and grid_filled attributes, but it does not
        return anything. In other languages like Java or C, this method would return
        void
        """

        ####### YOUR CODE HERE  ####### 
        # Hints my non-recursive solution contains one row-wise for loop, which contains 
        # several loops over individual lattice sites. You might need to visit each lattice 
        # site more than once per row. In my implementation, split the logic of checking
        # the von neumann neighborhood into a separate method _poll_neighbors, which
        # returns a boolean indicating whether a neighbor is filled
        #
        # My recursive solution calls a second function, _flow_recursive, which takes 
        # two lattice indices as arguments
        ###############################################################################

        # Fill first row
        self.grid_filled[0, self.grid[0] == 1] = 2

        # Iterate over remaining rows
        for i in range(1, self.n):

            # We do two passes over the row: forwards and backwards. Why do we need the 
            # second pass? Think about pathological site configurations that we might
            # miss in the first pass alone
            for j in np.hstack([np.arange(self.n), np.arange(self.n)[::-1]]):
                if self.grid[i, j] == 1:
                    if self._poll_neighbors(i, j):
                        self.grid_filled[i, j] = 2
            
            # Check to see if any sites in the current row are filled, and end the 
            # simulation early if none. This isn't necessary, but saves runtime
            # although the difference is a prefactor not a factor of N
            if np.all(self.grid_filled[i] != 2):
                break

        # Do a backwards pass over the grid to fill in any remaining sites. This step is
        # not necessary to determine whether the lattice percolates, but it is necessary
        # to make sure that our fill function finds all of the accessible sites

        for i in range(2, self.n):
            for j in np.hstack([np.arange(self.n), np.arange(self.n)[::-1]]):
                if self.grid[self.n - i, j] == 1:
                    if self._poll_neighbors(self.n - i, j):
                        self.grid_filled[self.n - i, j] = 2








    def percolate(self):
        """
        Initialize a random lattice and then run a percolation simulation. Report results
        """
        ###############################################################################

        ####### YOUR CODE HERE  ####### 
        # Hint: my solution is 3 lines of code, and it just calls other methods in the
        # class, which do the heavy lifting

        ###############################################################################
        
        # for i in range(self.n):
        #     self._flow2(0, i)

        # Run the flow algorithm and report the results
        self._flow()
        
        # return True if any site is full
        return np.any(self.grid_filled[-1] == 2) 



