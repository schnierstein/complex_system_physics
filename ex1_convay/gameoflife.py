################################################################################
# conway.py
#
# Author: electronut.in
#
# Description:
#
# A simple Python/matplotlib implementation of Conway's Game of Life.
################################################################################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 300
M = 600
ON = 1
OFF = 0
vals = [ON, OFF]

# populate grid with random on/off - more off than on
grid = np.random.choice(vals, N*M, p=[0.2, 0.8]).reshape(N, M)


def update(data):
    global grid

    top = np.roll(grid,1,axis=0)
    topleft = np.roll(top,1,axis=1)
    topright = np.roll(top,-1,axis=1)
    left = np.roll(grid,1,axis=1)
    right = np.roll(grid,-1,axis=1)
    bottom = np.roll(grid,-1,axis=0)
    bottomleft = np.roll(bottom,1,axis=1)
    bottomright = np.roll(bottom,-1,axis=1)

    total = (top+topleft+topright+left+right+bottom+bottomright+bottomleft)

    write0 = ((total < 2) | (total > 3)) | ((grid == 0) & (total == 2))
    write1 = ((grid == 1) & (total == 2)) | (total == 3)

    #newgrid = grid.copy()
    total[write0] = 0
    total[write1] = 1

    mat.set_data(total)
    grid = total
    return [mat]

# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50,
                              save_count=50)
plt.show()
