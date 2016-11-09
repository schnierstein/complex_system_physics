import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

N = 300
grid = 10
X = np.linspace(-grid,grid,N)

w0 = np.dstack(np.meshgrid(X, X)).reshape(-1, 2)

gamma = 3

t = np.linspace(0.,50.,100)

def f(w,t):
    x,y = w

    return [y, -1*gamma*y+x-x**3]


wsol = odeint(f,w0[0],t)

sol = np.array([[w0[0][0],w0[0][1],-1]])

print sol
for point in w0[1:]:
    wsol = odeint(f,point,t)

    if ((wsol[-1][0] <= -0.99) & (wsol[-1][0] >= -1.01)):
        sol = np.concatenate((sol,np.array([[point[0],point[1],-1]])))
    elif (((wsol[-1][0] <= 1.01) & (wsol[-1][0] >= 0.99))):
        sol = np.concatenate((sol,np.array([[point[0],point[1],1]])))
    else:
        sol = np.concatenate((sol,np.array([[point[0],point[1],0]])))


Z = np.array([e[2] for e in sol])

print len(Z)
plt.figure(1)
XX, YY = np.meshgrid(X,X)
C = Z.reshape(N,N)
plt.pcolormesh(XX,YY,C)
plt.colorbar()
plt.scatter([-1,1],[0,0],c= 'green',s=40,marker = 'x',edgecolors='green', label = 'Fix points')
plt.legend()
plt.axis([-grid,grid,-grid,grid])
plt.show()
