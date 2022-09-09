#!/usr/bin/python
import numpy as np




class AbelianSandpile:
    """
    An Abelian sandpile model simulation. The sandpile is initialized with a random
    number of grains at each lattice site. Then, a single grain is dropped at a random
    location. The sandpile is then allowed to evolve until it is stable. This process
    is repeated n_step times.
    
    Parameters:
    n (int): The size of the grid
    grid (np.ndarray): The grid of the sandpile
    history (list): A list of the sandpile grids at each timestep
    """


    def __init__(self, n=100, random_state=None):
        self.n = n
        np.random.seed(random_state) # Set the random seed
        self.grid = np.random.choice([0, 1, 2, 3], size=(n, n))
        self.history =[self.grid.copy()] # Why did we need to copy the grid?
        self.all_durations = list() # useful to keep track of the duration of toppling events

    def _add_and_topple(self, i, j):
        """
        A recursive function that adds a grain and then topples the sandpile at 
        location (i, j). Notice that we use the self.grid attribute to store global 
        information across all the   recursive calls. This is a common pattern in 
        recursive functions actingon lattices
        """
        self.grid[i, j] += 1

        # Base case
        if self.grid[i, j] < 4:
            return None
            
        else:
            # Decrease the height of the site
            self.grid[i, j] -= 4

            # Implement the absorbing boundary conditions: sandgrains
            # that fall off the edge of the grid are lost.
            if i > 0:
                self._add_and_topple(i - 1, j)
            if i < self.n - 1:
                self._add_and_topple(i + 1, j)
            if j > 0:
                self._add_and_topple(i, j - 1)
            if j < self.n - 1:
                self._add_and_topple(i, j + 1)
            return None

    def step(self):
        """
        Perform a single step of the sandpile model. Recall that there are two 
        timescales in this problem; step corresponds to the longer timescale of a 
        single sandgrain addition.

        A single step of the simulation consists of two stages: a random sand grain is 
        dropped onto the lattice at a random location. Then, a set of avalanches occurs
        causing sandgrains to get redistributed to their neighboring locations.

        Returns: None
        """
        ########## YOUR CODE HERE ##########
        #
        #
        # My solution starts by dropping a grain, and then solving for all topple events 
        # until the sandpile is stable. Watch your boundary conditions carefully.
        # We will use absorbing boundary conditions: excess sand grains fall off the edges
        # of the grid.
        #
        #
        ########## YOUR CODE HERE ##########

        # Pick a random location
        xi, yi = np.random.choice(self.n, 2)

        # Call the recursive topple function
        self._add_and_topple(xi, yi)

        ## Drop the grain and then topple the sand grains using an iterative solution:
        ## topple a site, then check the entire lattice for sites that need to be 
        # toppled. Repeat until the sandpile is stable.
        # self.grid[xi, yi] += 1
        # duration = 0
        # while np.any(self.grid >= 4):
        #     topple_inds = np.where(self.grid >= 4) # find a high site
        #     sel_ind = np.random.choice(np.arange(len(topple_inds[0])))
        #     ii, jj = (topple_inds[0][sel_ind], topple_inds[1][sel_ind])
        #     self.grid[ii, jj] -= 4
        #     if ii > 0:
        #         self.grid[ii - 1, jj] += 1
        #     if ii < self.n - 1:
        #         self.grid[ii + 1, jj] += 1
        #     if jj > 0:
        #         self.grid[ii, jj - 1] += 1
        #     if jj < self.n - 1:
        #         self.grid[ii, jj + 1] += 1
        #     duration += 1
        # if duration > 0:
        #     self.all_durations.append(duration)

        

    # we use this decorator for class methods that don't require any of the attributes 
    # stored in self. Notice how we don't pass self to the method
    @staticmethod
    def check_difference(grid1, grid2):
        """Check the total number of different sites between two grids"""
        return np.sum(grid1 != grid2)

    
    def simulate(self, n_step):
        """
        Simulate the sandpile model for n_step steps.
        """
        # YOUR CODE HERE. You should use the step method you wrote above.
        for i in range(n_step):
            self.step()
            if self.check_difference(self.grid, self.history[-1]) > 0:
                self.history.append(self.grid.copy())
        return self.grid

