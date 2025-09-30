import numpy as np

def random_unit_vec():
    """Return a random unit vector on S^2 (shape (3,))."""
    z = np.random.uniform(-1.0, 1.0)
    phi = np.random.uniform(0.0, 2.0 * np.pi)
    r = np.sqrt(max(0.0, 1.0 - z * z))
    return np.array([r * np.cos(phi), r * np.sin(phi), z], dtype=float)


class Bond:
    """Unit-length bond/tangent vector in R^3 with in-place rotations.

    Parameters:
        v (np.ndarray): Initial vector (shape (3,)); will be normalized.

    Attributes:
        v (np.ndarray): Unit vector (shape (3,)).

    Methods:
        rotate_in_place(axis: np.ndarray, angle: float): Rotate about an 
            arbitrary axis by Rodrigues' formula; re-normalize.
        copy(): Return a copy of the Bond.
    """

    def __init__(self, v):
        v = np.asarray(v, dtype=float).reshape(3)
        n = np.linalg.norm(v)
        if n == 0.0:
            raise ValueError("Zero vector is not allowed for Bond.")
        self.v = v / n

    def rotate_in_place(self, axis: np.ndarray, angle: float):
        """
        Given an arbitrary axis and angle, rotate a vector in place by Rodrigues' 
        formula, and then re-normalize.

        Args:
            axis (np.ndarray): Axis of rotation (shape (3,)).
            angle (float): Angle of rotation (radians).

        Returns:
            None
        """
        a = np.asarray(axis, dtype=float).reshape(3)
        na = np.linalg.norm(a)
        if na == 0.0:
            # Degenerate axis: no rotation
            return
        a /= na
        c, s = np.cos(angle), np.sin(angle)
        v = self.v
        # Rodrigues rotation
        v_rot = v * c + np.cross(a, v) * s + a * (np.dot(a, v)) * (1.0 - c)
        # Guard against FP drift
        self.v = v_rot / np.linalg.norm(v_rot)

    # Numpy interop: treat Bond like its vector
    def __array__(self, dtype=None):
        return np.asarray(self.v, dtype=dtype)

    def copy(self):
        return Bond(self.v.copy())


class WormlikeChainMC:
    """Discrete 3D wormlike chain with Metropolis updates in tangent space.

    The chain is represented by N unit bond vectors (Bond objects) of fixed length b.
    Positions are reconstructed by r_{k+1} = r_k + b t_k (with r_0 at the origin).
    Bending energy: E = kappa * sum_i (1 - t_i · t_{i+1}).

    Parameters:
        N (int): Number of bonds.
        b (float): Bond length (segment length).
        kappa (float): Bending stiffness (k_B T units). Persistence length l_p = kappa * b.
        beta (float): Inverse temperature 1/T (k_B=1).
        random_state (int | None): Random state for numpy.random.

    Attributes:
        N (int): Number of bonds.
        b (float): Bond length.
        kappa (float): Bending stiffness.
        beta (float): Inverse temperature.
        bonds (list[Bond]): List of N Bond instances (unit vectors).
    """
    def __init__(self, N=400, b=1.0, kappa=20.0, beta=1.0, random_state=None):
        self.N, self.b = int(N), float(b)
        self.kappa, self.beta = float(kappa), float(beta)
        self.random_state = random_state
        np.random.seed(random_state)

        ## start nearly straight with small transverse noise, then normalize per Bond
        base = np.tile(np.array([1.0, 0.0, 0.0], dtype=float), (self.N, 1))
        base += 0.05 * np.random.normal(size=base.shape)
        self.bonds = [Bond(v) for v in base]

        ## calculate the persistence length
        self.lp = self.kappa * self.b * self.beta

    def tangent_vectors(self):
        """Stack current bond vectors into a (N, 3) ndarray."""
        return np.vstack([b.v for b in self.bonds])

    def positions(self):
        """Return positions r_k, k=0..N as shape (N+1,3) with r_0 = 0."""
        r = np.zeros((self.N + 1, 3), dtype=float)
        np.cumsum(self.b * self.tangent_vectors(), axis=0, out=r[1:])
        return r

    def energy(self):
        """Compute the total bending energy of the chain."""
        t = self.tangent_vectors()
        dots = (t[:-1] * t[1:]).sum(axis=1)
        return float(self.kappa * np.sum(1.0 - dots))

    def _local_deltaE(self, i: int, trial_vec: np.ndarray):
        """Energy change from replacing t_i by trial_vec (only neighbors matter)."""
        # ################################################################################
        # #
        # #
        # #  YOUR CODE HERE
        # # 
        # # Be sure to watch out for boundary conditions on the chain.
        # #
        # #
        # ################################################################################
        # raise NotImplementedError("Implement this method")
    
        dE = 0.0
    
        # Compute the change in energy due to the neighbor on the left, skipping
        # the first bonds.
        if i > 0:
            dE += self.kappa * ((1.0 - float(np.dot(trial_vec, self.bonds[i - 1].v)))
                                - (1.0 - float(np.dot(self.bonds[i].v, self.bonds[i - 1].v))))
            
        # Compute the change in energy due to the neighbor on the right, skipping
        # the last bond.
        if i < self.N - 1:
            dE += self.kappa * ((1.0 - float(np.dot(trial_vec, self.bonds[i + 1].v)))
                                - (1.0 - float(np.dot(self.bonds[i].v, self.bonds[i + 1].v))))
            
        return float(dE)

    def sweep(self, step_size: float = 0.3):
        """
        One Monte Carlo sweep consists of attempting N local rotations, one for each 
        bond on the chain.

        Args:
            step_size (float): Typical rotation angle (radians) for proposals.

        Returns:
            dict: {'acc': float, 'E': float} The fraction of moves that were accepted
                and the final energy of the chain after the sweep.
        """
        # ################################################################################
        # #
        # #
        # #  YOUR CODE HERE
        # #
        # # Your implementation should visit each bond once, propose a new bond, calculate
        # # the change in energy, and then accept or reject the proposed move using a 
        # # Metropolis acceptance test. Be sure to use the copy method of the Bond object
        # # to propose a new bond, to avoid modifying the original bond in place.
        # #
        # #  Your implementation should keep a counter of the number of accepted moves, so
        # #  that you can return the acceptance rate as part of the return value. This is
        # #  useful for diagnosing the hyperparameters of the Monte Carlo simulation.
        # # 
        # #  You should also compute the final energy of the chain after the sweep, so
        # #  that you can return that as part of the return value.
        # #
        # ################################################################################
        # raise NotImplementedError("Implement this method")
    
        num_accepted = 0
        for _ in range(self.N):

            ## Sample parameters of random update
            i = np.random.randint(self.N)  # choose a random bond
            axis = random_unit_vec()      # choose a random axis
            angle = np.random.normal(scale=step_size) # choose a random angle

            ## propose a rotated vector by copying the bond and rotating it
            trial = self.bonds[i].copy()
            trial.rotate_in_place(axis, angle)
            t_new = trial.v  # Unit length by construction

            ## Compute the change in energy from the proposed move
            dE = self._local_deltaE(i, t_new)

            ## Use the Metropolis acceptance test to determine whether to accept the move
            if dE <= 0.0 or np.random.random() < np.exp(-self.beta * dE):
                # accept: rotate in place (keeps unit length by construction)
                self.bonds[i].rotate_in_place(axis, angle)
                num_accepted += 1
                
        return {"accepted fraction": num_accepted / self.N, "E": self.energy()}

    def end_to_end(self):
        """Return end-to-end vector R and its squared length."""
        R = self.b * self.tangent_vectors().sum(axis=0)
        return R, float(np.dot(R, R))

    def tangent_correlation(self):
        """Compute C(s) = <t_i · t_{i+s}> averaged over i.

        Returns:
            (np.ndarray, np.ndarray): separations s, correlations C(s).
        """
        max_sep = (self.N - 1) // 4 # Largest separation is 1/4 of chain length
        s_vals = np.arange(0, max_sep + 1, dtype=int)
        t = self.tangent_vectors()
        C = np.zeros_like(s_vals, dtype=float)
        for si, s in enumerate(s_vals):
            dots = (t[: self.N - s] * t[s:]).sum(axis=1)
            C[si] = float(np.mean(dots))
        return s_vals, C
    

    def simulate(self, n_eq, step_size=0.25):
        """
        Simulate the wormlike chain and return self

        Args:
            n_eq (int): Number of of sweeps to equilibrate the chain.
            step_size (float): Proposal rotation angle scale (radians).

        Returns:
            dict: {'E': np.ndarray, 'R2': np.ndarray, 'acc': np.ndarray, 't_corr': (s, C), 'chain': WormlikeChainMC}
        """
        for _ in range(n_eq):
            self.sweep(step_size=step_size)
        return self
