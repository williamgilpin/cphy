#!/usr/bin/python
import numpy as np
from scipy.integrate import solve_ivp

class AllenCahn:
    """
    Simulate the two-dimensional Allen-Cahn model using spectral methods
    """
    def __init__(self, nx, ny, d=1.0, kappa=1.0, Lx=1.0, Ly=1.0):
        self.nx, self.ny = nx, ny
        self.dx = Lx / nx
        self.dy = Ly / ny
        self.d = d
        self.kappa = kappa
        
        kx = (np.pi / Lx) * np.hstack([np.arange(nx / 2 + 1), np.arange(1 - nx / 2, 0)])
        ky = (np.pi / Ly) * np.hstack([np.arange(ny / 2 + 1), np.arange(1 - ny / 2, 0)])
        self.kx, self.ky = kx, ky

        kxx, kyy = np.meshgrid(kx, ky)
        ksq = kxx**2 + kyy**2
        self.ksq = ksq.flatten()

        
    def _reaction(self, y):
        """
        Bistable reaction term: cast into real space, perform reaction, and then cast
        back into Fourier space.
        """
        ################################################
        #
        # Your code here. I recommend performing the reaction in real space, and using
        # the appropriate transformations to cast back and forth within the function.
        #
        ################################################
        y = np.reshape(y, (self.ny, self.nx))
        yh = np.fft.ifft2(y)
        out = np.fft.fft2(yh * (1 - yh**2))
        return out.flatten()

    def rhs(self, t, y):
        """
        For technical reasons, this function needs to take a one-dimensional vector, 
        and so we have to reshape the vector back into the mesh
        """
        return self.kappa * self._reaction(y) - self.d * self.ksq  * y


    def solve(self, y0, t_min, t_max, nt, **kwargs):
        """
        Solve the heat equation using the odeint solver

        **kwargs are passed to scipy.integrate.solve_ivp
        """
        tpts = np.linspace(t_min, t_max, nt)
        y0_k = np.fft.fft2(y0)

        out = solve_ivp(self.rhs, (t_min, t_max), y0_k.flatten(), t_eval=tpts, **kwargs)
        sol = out.y.T
        tpts =  out.t

        ## Convert back to real space
        sol2 = list()
        for row in sol:
            sol2.append(np.fft.ifft2(row.reshape((self.nx, self.ny))))
        sol2 = np.array(sol2)
        print(f"Sanity check: imaginary residual is: {np.mean(np.abs(np.imag(np.array(sol2))))}")
        sol2 = np.real(sol2)
        sol = sol2

        return tpts, sol




