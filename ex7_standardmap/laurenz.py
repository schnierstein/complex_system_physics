import numpy as np
import matplotlib.pyplot as plt

# standard map:
def standard_map(x, p, K):
    new_x = (x+p)%1
    new_p = p+K/(2*np.pi)*np.sin(2*np.pi*new_x)
    return new_x, new_p

# constants:
K = np.pi/4.0
Nx = 10
Ny = 20
iterations = 1000
pointsize = 0.05


plt.figure()
# create grid:
xGrid, pGrid = np.meshgrid(np.linspace(0,1, Nx+1), np.linspace(-1,1, Ny+1))

plt.scatter(xGrid, pGrid, marker = ".", s = pointsize, alpha = 1, color = "0.0", antialiased=True)
# for each tuple in grid iterate to the next step and plot all points:
for i in range(iterations):
    xGrid, pGrid = standard_map(xGrid, pGrid, K)
    plt.scatter(xGrid, pGrid, marker = ".", s = pointsize, alpha = 1, color = "0.0", antialiased=True)

plt.axis([0,1, -1, 1])
plt.title("Phase Space of Standard Map with K = %.3f and %d iterations" % (K, iterations))
plt.xlabel('x')
plt.ylabel('p')
plt.show()
