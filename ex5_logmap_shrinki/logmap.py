import numpy as np
import matplotlib.pyplot as plt

def logpoints(r,t,start):
    x = start

    points = np.empty(t)
    rs = np.empty(t)

    for i in xrange(t):
        points[i] = x
        rs[i] = r
        x = r * x * (1-x)
    return [rs,points]

plt.figure(1)

for r in np.linspace(2,4,2000):
    points = logpoints(r,2000,0.5)
    plt.plot(points[0][-100:],points[1][-100:], '.', color = 'black', markersize = 0.5)

plt.show()
