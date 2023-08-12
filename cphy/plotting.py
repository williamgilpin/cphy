import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plt_sphere(pts, radius, ax=None):
    """
    Plot a set of spheres with given centers and radii.

    Args:
        pts (ndarray): the centers of the spheres
        radius (float): the radius of the spheres
        ax (Axes3D): the axes on which to plot the spheres

    Returns:
        ax (Axes3D): the axes on which the spheres were plotted

    """
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

    for pt in pts:
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = radius * np.outer(np.cos(u), np.sin(v)) + pt[0]
        y = radius * np.outer(np.sin(u), np.sin(v)) + pt[1]  
        z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + pt[2]
        # Plot sphere surfaces    
        ax.plot_surface(x, y, z, color='b', alpha=0.8)
    
    return ax