import numpy as np

N = 5
ON = 1
OFF = 0
vals = [ON,OFF]

grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

print grid


top = np.roll(grid,1,axis=0)
topleft = np.roll(top,1,axis=1)
topright = np.roll(top,-1,axis=1)
left = np.roll(grid,1,axis=1)
right = np.roll(grid,-1,axis=1)
bottom = np.roll(grid,-1,axis=0)
bottomleft = np.roll(bottom,1,axis=1)
bottomright = np.roll(bottom,-1,axis=1)

total = top+topleft+topright+left+right+bottom+bottomright+bottomleft

wright0 = ((total < 2) | (total > 3)) | ((grid == 0) & (total == 2))
wright1 = ((grid == 1) & (total == 2)) | (total == 3)

newgrid = grid
newgrid[wright0] = 0
newgrid[wright1] = 1

print newgrid
