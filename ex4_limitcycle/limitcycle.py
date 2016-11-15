import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

a = 1
grid = 2.

X,Y = np.meshgrid(np.arange(-grid,grid,0.2),np.arange(-grid,grid,0.2))

U = Y
V = -a*Y*(X**2+Y**2-1) - X

def f(w,t):
    x,y = w
    return [y,-a*y*(x**2+y**2-1) - x]

w0 = [[-1.5,-1.5],[-1.5,1.5],[1.5,1.5],[1.5,-1.5],[-0.3,-0.3],[0.3,0.3],[-0.3,0.3],[0.3,-0.3]]


plt.figure(1)

t = np.linspace(0.,7.,300.)
j = 1
for point in w0:
    print point
    wsol = odeint(f,point,t)
    plt.plot([e[0] for e in wsol],[e[1] for e in wsol],c = 'red',linewidth = 1)

    j = j+1

plt.plot([e[0] for e in w0],[e[1] for e in w0],'x',label = 'Startpoints')
plt.axis([-grid,grid,-grid,grid])

#plt.streamplot(X,Y,U,V,density=0.5)

plt.show()
