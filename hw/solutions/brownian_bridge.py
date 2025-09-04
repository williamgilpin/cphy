#!/usr/bin/python
import numpy as np


class BridgeBaseClass:
    """
    Simulate a stochastic process that is pinned to start and end at fixed values 
    over a fixed interval.

    Parameters
        T (float): The total time of the simulation.
        a (float): The starting value of the process.
        b (float): The ending value of the process.
    """

    def __init__(self, T=1.0, a=0.0, b=0.0):
        self.T = T
        self.a = a
        self.b = b
        print(
            "Running with Instructor Solutions. If you meant to run your own code, do not import from solutions", 
            flush=True
        )

    def simulate(self, n_steps):
        """Implement the simulation method. Override this method in subclasses."""
        pass

class BrownianBridgeRejection(BridgeBaseClass):
    """
    Simulate a Brownian bridge by rejection sampling.

    Parameters
        n_rejections (int): The number of rejection samples to take.
        *args, **kwargs: Additional arguments to pass to the parent class.
    """

    def __init__(self, n_rejections, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n_rejections = n_rejections

    def simulate(self, n_steps):
        """Simulate a Brownian bridge.
        
        Args:
            n_steps (int): The number of steps to simulate.

        Returns
            np.ndarray: A 1D array of shape (n_steps) containing the simulated 
                Brownian bridge.
        """
        steps = np.random.normal(size=(self.n_rejections, n_steps))
        walks = np.cumsum(steps, axis=1) # cumulative sum into walks[:, 1:]
        closest_return = np.argmin(np.abs(walks[:, -1] - self.b), axis=0)
        return walks[closest_return]
    
class BrownianBridgeTransform(BridgeBaseClass):
    """
    Simulate a Brownian bridge by using a transformation of standard Brownian motion.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def simulate(self, n_steps):
        """Simulate a Brownian bridge using a transformation of standard Brownian motion."""
        steps = np.random.normal(size=(n_steps))
        walk = np.cumsum(steps)
        walk = np.concatenate([[0], walk])
        t = np.linspace(0, self.T, n_steps + 1)
        bridge = walk - t * walk[-1]
        return bridge





