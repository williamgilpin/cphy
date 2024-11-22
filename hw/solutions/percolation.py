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
    + For boundary conditions, assume that any site out of bounds is a 0 (blocked)
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
        np.random.seed(random_state)
        # Initialize a random grid if one is not provided. Otherwise, use the provided
        # grid.
        if grid is None:
            self.n = n
            self.p = p
            self.grid = np.random.choice([0, 1], size=(n, n), p=[p, 1 - p])

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


    def _flow_recursive(self, i, j):
        """
        The recursive portion of the flow simulation.
        This function checks if water can flow to the current site (i, j),
        and if it can, it will mark the site as filled (2).
        Then it will check the neighboring sites (above, below, left, right)
        recursively.
        """

        # Base case: Stop if we are out of bounds or the site is already filled.
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return  # Out of bounds
        if self.grid_filled[i, j] != 1:
            return  # Site is either blocked (0) or already filled (2)

        # Fill the current site with water
        self.grid_filled[i, j] = 2

        # Recursively flow into neighboring sites
        self._flow_recursive(i-1, j)  # Check the site above
        self._flow_recursive(i+1, j)  # Check the site below
        self._flow_recursive(i, j-1)  # Check the site to the left
        self._flow_recursive(i, j+1)  # Check the site to the right

        return True


    def percolate(self):
        """
        Run the percolation simulation and return True if the system percolates.
        """
        for j in range(self.n):
            if self.grid_filled[0, j] == 1:  # Start the flow from the top row
                self._flow_recursive(0, j)

        # Check if any water reached the bottom row
        return np.any(self.grid_filled[-1, :] == 2)

##Octavio was here
