#!/usr/bin/python
import numpy as np
from scipy.integrate import solve_ivp


def make_initial_conditions(n):
    """
    Make a bump-shaped initial conditions array
    """
    xx, yy = np.meshgrid(np.linspace(-1, 1, n), np.linspace(-1, 1, n))
    rr =  (xx**2 + yy**2)**0.5
    u_ic = 1 - 0.5 * np.copy(np.exp(-rr**2 - xx**2))
    v_ic = 0.25 * np.copy(np.exp(-rr**2))
    return u_ic, v_ic

class GrayScott:
    """
    Simulate the two-dimensional Gray-Scott model
    """
    # def __init__(self, nx, ny, du=0.1, dv=0.05, b=0.0545, kappa=0.1, Lx=1.0, Ly=1.0):
    def __init__(self, nx, ny, du=0.1, dv=0.05, b=0.0545, kappa=0.1165, Lx=1.0, Ly=1.0):
        self.nx, self.ny = nx, ny
        self.dx = Lx / nx
        self.dy = Ly / ny
        self.du, self.dv = du, dv
        self.kappa = kappa
        self.b = b
        
        kx = (np.pi / Lx) * np.hstack([np.arange(nx / 2 + 1), np.arange(1 - nx / 2, 0)])
        ky = (np.pi / Ly) * np.hstack([np.arange(ny / 2 + 1), np.arange(1 - ny / 2, 0)])
        self.kx, self.ky = kx, ky

        kxx, kyy = np.meshgrid(kx, ky)
        ksq = kxx**2 + kyy**2
        self.ksq = ksq.flatten()

        # These are some speed hacks. Instead of repeatedly flattening and then reshaping
        # the arrays, we can just augment our parameter array. We gain speed at the 
        # expense of memory.
        self.d = np.hstack([self.du * np.ones(nx * ny), self.dv * np.ones(nx * ny)])
        self.ksq_stack = np.hstack([self.ksq, self.ksq])
        
    def _reaction(self, y):
        """
        Bistable reaction term: cast into real space, perform reaction, and then cast
        back into Fourier space.
        """
        ########
        #
        # Your code here. I recommend performing the reaction in real space, and using
        # the appropriate transformations to cast back and forth within the function.
        #
        ########

        # uvv = u*v*v
        # u += Du*Lu - uvv + F*(1 - u)
        # v += Dv*Lv + uvv - (F + k)*v

        u = np.fft.ifft2(np.reshape(y[:self.nx * self.ny], (self.nx, self.ny)))
        v = np.fft.ifft2(np.reshape(y[-self.nx * self.ny:], (self.nx, self.ny)))

        # u = np.real(u)
        # v = np.real(v)

        uv2 = u * (v**2)
        rxn_u = -uv2 + self.b * (1 - u)
        rxn_v = uv2 - self.kappa * v

        uk_out = np.fft.fft2(rxn_u)
        vk_out = np.fft.fft2(rxn_v)
        yk_out = np.hstack([uk_out.flatten(), vk_out.flatten()])
        return yk_out


    def _diffusion(self, y):
        """
        Perform diffusion in Fourier space
        """
        ########
        #
        # Your code here. My solution is one line, but it depends on how you handle 
        # the two different diffusion coefficients.
        #
        ########

        return -self.d * self.ksq_stack * y
       # return -self.d * self.ksq_stack  * y

    def rhs(self, t, y):
        """
        For technical reasons, this function needs to take a one-dimensional vector, 
        and so we have to reshape the vector back into the mesh
        """
        # uv2 = u * (v**2)
        # rhs_u = -uv2 + a * (1 - u)
        # rhs_v = uv2 - b * v
        # return rhs_u, rhs_v
        #y = y.reshape((self.ny, self.nx))

        out = 10*self._reaction(y) + self._diffusion(y)

        return out


    def solve(self, y0, t_min, t_max, nt, **kwargs):
        """
        Solve the heat equation using the odeint solver

        **kwargs are passed to scipy.integrate.solve_ivp
        """
        u0, v0 = y0
        tpts = np.linspace(t_min, t_max, nt)
        u0k, v0k = np.fft.fft2(u0), np.fft.fft2(v0) # initial condition in Fourier space
        y0k = np.hstack([u0k.flatten(), v0k.flatten()])

        out = solve_ivp(self.rhs, (t_min, t_max), y0k, t_eval=tpts, **kwargs)
        sol = out.y.T

        # convert back to real space
        sol2 = list()
        for row in sol:
            sol2.append([
                np.fft.ifft2(np.reshape(row[:self.nx * self.ny], (self.nx, self.ny))),
                np.fft.ifft2(np.reshape(row[-self.nx * self.ny:], (self.nx, self.ny)))
            ])
        sol2 = np.moveaxis(np.array(sol2), 1, 3)

        return tpts, sol2


