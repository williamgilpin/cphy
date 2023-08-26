import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

high_contrast = [
    [0.372549, 0.596078, 1], 
    [1.0, .3882, .2784], 
    [0.20784314, 0.67843137, 0.6], 
    [0.59607843, 0.25882353, 0.89019608],
    [0.803922, 0.0627451, 0.462745], 
    [0.917647, 0.682353, 0.105882],
    [0.7, 0.7, 0.7]
]
blue, red, turquoise, purple, magenta, orange, gray  = high_contrast

pastel_rainbow = np.array([
    [221, 59,  53],
    #[211, 132, 71],
    [237, 157, 63],
    [165, 180, 133],
    [63,  148, 109], 
    [50,  122, 137], 
    [44,  115, 178], 
    [43,  52,  124],
    [164, 36, 124],
    [186, 173, 214],
    # [191, 163, 215],
    # [139,  211, 126],
    [163, 218, 133],
    [136, 159, 122],
    [168, 192, 221]
])/255.

pastel_rainbow_alt = pastel_rainbow[[0, 5, 3, 1, 7, 4, 2, 8, 6, 9, 10, 11]]

# degas line plot colors
royal_purple = np.array((120, 81, 169))/255.

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

from ipywidgets import interact, IntSlider, Layout
from IPython.display import display, clear_output
def sliderplot(arr, figsize=(6, 6), width='100%', **kwargs):
    """
    Given a 3-dimensional array, plot the last two dimensions and make a slider along
    the first dimension.

    Args:
        arr (ndarray): a 3-dimensional array
        figsize (tuple): the size of the figure
        width (str): the width of the slider
        **kwargs: keyword arguments to pass to plt.imshow
    """

    n = arr.shape[0]
    def plotter(i):
        plt.close()
        fig = plt.figure(figsize=figsize)
        plt.imshow(arr[i], **kwargs);
        plt.show()
    interact(
        plotter, 
        i=IntSlider(
            min=0, max=n-1, step=1, value=0, layout=Layout(width=width)
        )
    );
    

def vanish_axes(gca=None):
    """Make all axes disappear from a plot"""
    if not gca:
        gca = plt.gca()
    gca.set_axis_off()
    gca.xaxis.set_major_locator(plt.NullLocator())
    gca.yaxis.set_major_locator(plt.NullLocator())
