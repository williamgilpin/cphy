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
    all_durations (list): A list of the durations of each avalanche
    """

    def __init__(self, n=100, random_state=None):
        self.n = n
        np.random.seed(random_state) # Set the random seed
        self.grid = np.random.choice([0, 1, 2, 3], size=(n, n))
        self.history =[self.grid.copy()] # Why did we need to copy the grid?
        self.all_durations = list() # useful to keep track of the duration of toppling events


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
        #  until the sandpile is stable. Watch your boundary conditions carefully.
        #
        # I'd recommend using a while loop for the toppling events
        # We will use absorbing boundary conditions: excess sand grains fall off the edges
        # of the grid.
        # In addition to updating self.grid, keep track of the topple durations in the 
        # instance variable self.all_durations
        #
        #
        ########## YOUR CODE HERE ##########

        # Drop a grain at a random location
        xi, yi = np.random.choice(self.n, 2)
        self.grid[xi, yi] += 1

        # Topple the sand grains
        duration = 0
        while np.any(self.grid >= 4):
            topple_inds = np.where(self.grid >= 4)
            sel_ind = np.random.choice(np.arange(len(topple_inds[0])))
            ii, jj = (topple_inds[0][sel_ind], topple_inds[1][sel_ind])
            self.grid[ii, jj] -= 4
            if ii > 0:
                self.grid[ii - 1, jj] += 1
            if ii < self.n - 1:
                self.grid[ii + 1, jj] += 1
            if jj > 0:
                self.grid[ii, jj - 1] += 1
            if jj < self.n - 1:
                self.grid[ii, jj + 1] += 1
            duration += 1
        if duration > 0:
            self.all_durations.append(duration)

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



# vals, bins = np.histogram(all_avalanche_sizes, bins=np.logspace(np.log10(4), np.log10(1000), 50))
# plt.figure()
# plt.semilogy(bins[:-1], vals, '.', markersize=10)
# plt.title('Avalanche size distribution')
# plt.xlabel('Avalanche size')
# plt.ylabel('Count')

# vals, bins = np.histogram(all_avalanche_durations)
# plt.figure()
# plt.loglog(bins[:-1], vals, '.',  markersize=10)
# # plt.loglog(bins[:-1], (vals[0] / bins[0]) * bins[:-1]**(-1), '-k') # plot 1/T scaling

