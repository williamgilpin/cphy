#!/usr/bin/python
import numpy as np


# DFS: O(N_v + N_E)

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
        store_history (bool): Whether or not to store the history of the sandpile. Snapshots
            of the sandpile are stored between avalanche events
    """


    def __init__(self, n=100, random_state=None, store_history=True):
        self.n = n
        np.random.seed(random_state) # Set the random seed
        self.grid = np.random.choice([0, 1, 2, 3], size=(n, n))
        self.history =[self.grid.copy()] # Why did we need to copy the grid?
        self.all_durations = list() # useful to keep track of the duration of toppling events
        self.store_history = store_history
        print(
            "Running with Instructor Solutions. If you meant to run your own code, do not import from solutions", 
            flush=True
        )

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
        # Pick a random location
        xi, yi = np.random.choice(self.n, 2)

        # Drop the grain and then topple the sand grains using an iterative solution:
        # topple a site, then check the entire lattice for sites that need to be 
        # toppled. Repeat until the sandpile is stable.
        self.grid[xi, yi] += 1
        duration = 0
        while np.any(self.grid >= 4):
            topple_inds = np.where(self.grid >= 4) # find a high site
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



class AbelianSandpileIterative(AbelianSandpile):
    """
    An Abelian sandpile model simulation. The sandpile is initialized with a random
    number of grains at each lattice site. Then, a single grain is dropped at a random
    location. The sandpile is then allowed to evolve until it is stable. This process
    is repeated n_step times.
    
    Parameters:
        n (int): The size of the grid
        grid (np.ndarray): The grid of the sandpile
        history (list): A list of the sandpile grids at each timestep
        store_history (bool): Whether or not to store the history of the sandpile. Snapshots
            of the sandpile are stored between avalanche events
    """


    def __init__(self, n=100, random_state=None):
        super().__init__(n, random_state)
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
        # Pick a random location
        xi, yi = np.random.choice(self.n, 2)

        # Drop the grain and then topple the sand grains using an iterative solution:
        # topple a site, then check the entire lattice for sites that need to be 
        # toppled. Repeat until the sandpile is stable.
        self.grid[xi, yi] += 1
        duration = 0
        while np.any(self.grid >= 4):
            topple_inds = np.where(self.grid >= 4) # find a high site
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




class AbelianSandpileDFS(AbelianSandpile):
    """
    An alternative implementation of the Abelian Sandpile model using a depth-first
    search algorithm to find all sites that need to be toppled.

    Parameters:
        n (int): The size of the grid
        grid (np.ndarray): The grid of the sandpile
        history (list): A list of the sandpile grids at each timestep
        store_history (bool): Whether or not to store the history of the sandpile. Snapshots
            of the sandpile are stored between avalanche events
    """


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _add_and_topple(self, i, j):
        """
        A recursive function that adds a grain and then topples the sandpile at 
        location (i, j). Notice that we use the self.grid attribute to store global 
        information across all the   recursive calls. This is a common pattern in 
        recursive functions actingon lattices
        """
        self.grid[i, j] += 1 # global state update

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
        # Pick a random location
        xi, yi = np.random.choice(self.n, 2)
        # Call the recursive topple function
        self._add_and_topple(xi, yi)


from collections import deque
class AbelianSandpileBFS(AbelianSandpile):
    """
    An alternative implementation of the Abelian Sandpile model using a breadth-first
    search algorithm to find all sites that need to be toppled.

    An advantage of this implementation is that it it matches the physics of the 
    sandpile model more closely. In particular, grains get passed to sites 
    simultaneously, rather than sequentially as in the DFS implementation.

    We therefore define a separate history attribute in order to record the fast-timescale 
    topple events that occur between grain additions.

    Parameters:
        n (int): The size of the grid
        grid (np.ndarray): The grid of the sandpile
        history (list): A list of the sandpile grids at each timestep
        store_history (bool): Whether or not to store the history of the sandpile. Snapshots
            of the sandpile are stored between avalanche events
    """

    def __init__(self, store_topple_history=False, **kwargs):
        super().__init__(**kwargs)
        self.store_topple_history = store_topple_history
        if store_topple_history:
            self.history_topples = [self.grid.copy()]

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
        # Pick a random location
        xi, yi = np.random.choice(self.n, 2)

        # A queue data structure stores a list of sites that need to be toppled.
        queue = deque([(xi, yi)])
        
        # Perform a breadth-first search to find all sites that need to be toppled
        # the while loop will continue until the queue is empty
        while queue:
            # the popleft() method removes the first element from the queue
            i, j = queue.popleft()
            self.grid[i, j] += 1 # global state update

            # Base case
            if self.grid[i, j] < 4:
                continue
        
            # Store a snapshot if a topple event occurs
            if self.store_topple_history:
                self.history_topples.append(self.grid.copy())

            # Decrease the height of the site
            self.grid[i, j] -= 4

            # Implement the absorbing boundary conditions: sand grains
            # that fall off the edge of the grid are lost.
            if i > 0:
                queue.append((i - 1, j))
            if i < self.n - 1:
                queue.append((i + 1, j))
            if j > 0:
                queue.append((i, j - 1))
            if j < self.n - 1:
                queue.append((i, j + 1))
