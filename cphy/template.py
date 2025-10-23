import matplotlib.pyplot as plt

## set default font Helvetica
plt.rcParams['font.family'] = 'Helvetica'

## Set nicer colors
plt.rcParams['image.cmap'] = 'PuBu'
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[[1.0, .3882, .2784]])
plt.rcParams['lines.markersize'] = 10


## In-notebook video settings
plt.rcParams["animation.writer"] = "ffmpeg"
plt.rcParams["animation.bitrate"] = 800                     # kb/s cap
plt.rcParams["animation.ffmpeg_args"] = [                   # finer control
    "-crf", "24",        # 18–28 is common; larger = smaller file
    "-preset", "slow",   # slower = better compression
    "-pix_fmt", "yuv420p"
]
plt.rcParams["animation.embed_limit"] = 25


## Plot legend style
plt.rcParams['legend.frameon'] = False
plt.rcParams['legend.facecolor'] = 'none'
plt.rcParams['legend.edgecolor'] = 'none'