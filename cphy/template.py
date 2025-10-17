import matplotlib.pyplot as plt

## set default font Helvetica
plt.rcParams['font.family'] = 'Helvetica'

## Set nicer colors
plt.rcParams['image.cmap'] = 'PuBu'
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[[1.0, .3882, .2784]])
plt.rcParams['lines.markersize'] = 10
