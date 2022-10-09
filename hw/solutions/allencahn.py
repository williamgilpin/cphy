#!/usr/bin/python
import numpy as np




from scipy.integrate import odeint, solve_ivp

class AllenCahn:
    """
    An implementation of the Allen-Cahn equation in two dimensions, using the method
    of lines and explicit finite differences

    Parameters
        nx (int): number of grid points in the x direction
        ny (int): number of grid points in the y direction
        kappa (float): reaction rate
        d (float): diffusion coefficient
        Lx (float): length of the domain in the x direction
        Ly (float): length of the domain in the y direction

    """

    def __init__(self, nx, ny, kappa=1.0, d=1.0, Lx=1.0, Ly=1.0):
        self.nx = nx
        self.ny = ny
        self.dx = Lx / nx
        self.dy = Ly / ny
        self.d = d
        self.kappa = kappa
       
    def _laplace(self, grid):
        """
        Apply the two-dimensional Laplace operator to a square array
        """
        ################################################################################
        #
        #
        #  YOUR CODE HERE
        #  My 10 line solution is vectorized in numpy, and so it avoids using a for loop 
        #  There are several valid ways to implement the boundary conditions
        #
        ################################################################################
        
        lap = np.zeros((self.ny, self.nx))

        # enforce reflection boundary conditions by padding rows and columns
        grid = np.vstack([grid[0, :][None, :], grid, grid[-1, :][None, :]])
        grid  = np.hstack([grid[:, 0][:, None], grid, grid[:, -1][:, None]])

        lap = grid[:-2, 1:-1] + grid[1:-1, :-2] + grid[2:, 1:-1] + grid[1:-1, 2:]
        lap  -= 4 * grid[1:-1, 1:-1]
        
        lap /= self.dx * self.dy
        return lap

    def _reaction(self, y):
        """
        Bistable reaction term
        """
        ################################################################################
        #
        #
        #  YOUR CODE HERE.
        #
        #
        ################################################################################
        return y * (1 - y**2)

    def rhs(self, t, y):
        """
        For technical reasons, this function needs to take a one-dimensional vector, 
        and so we have to reshape the vector back into the mesh
        """
        ################################################################################
        #
        #
        #  YOUR CODE HERE
        #  My solution primariy calls private methods
        #
        #
        ################################################################################
        y = y.reshape((self.ny, self.nx))
        out = self.kappa * self._reaction(y) + self.d * self._laplace(y)
        return out.flatten()


    def solve(self, y0, t_min, t_max, nt, **kwargs):
        """
        Solve the heat equation using the odeint solver

        **kwargs are passed to scipy.integrate.solve_ivp
        """
        ################################################################################
        #
        #
        #  YOUR CODE HERE
        #  My solution is five lines, and it mainly involves setting things up to be
        #  passed to scipy.integrate.solve_ivp, and then returning the results
        #
        #
        ################################################################################
        tpts = np.linspace(t_min, t_max, nt)
        out = solve_ivp(self.rhs, (t_min, t_max), y0.flatten(), t_eval=tpts, **kwargs)
        sol = out.y.T
        tpts =  out.t
        return tpts, sol.reshape((len(tpts), self.ny, self.nx))




