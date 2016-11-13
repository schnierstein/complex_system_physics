import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

N = 300
grid = 10
X = np.linspace(-grid,grid,N)

w0 = np.dstack(np.meshgrid(X, X)).reshape(-1, 2)

# for going backwards in time use negative gamma
gamma = 0.5

t = np.linspace(0.,50.,100)

def f(w,t):
    x,y = w

    return [y, -1*gamma*y+x-x**3]

def g(w,t):
    x,y = w
    return [-y, gamma*y-x+x**3]

wsol = odeint(f,w0[0],t)

sol = np.array([[w0[0][0],w0[0][1],wsol[-1][0]]])
k = 1
p = 1
for point in w0[1:]:

    if (k/1000 == p):
        print k
        p = p+1
    k = k+1
    wsol = odeint(f,point,t)

    if ((wsol[-1][0] <= -0.99) & (wsol[-1][0] >= -1.01)):
        sol = np.concatenate((sol,np.array([[point[0],point[1],-1]])))
    elif (((wsol[-1][0] <= 1.01) & (wsol[-1][0] >= 0.99))):
        sol = np.concatenate((sol,np.array([[point[0],point[1],1]])))
    else:
        sol = np.concatenate((sol,np.array([[point[0],point[1],0]])))


Z = np.array([e[2] for e in sol])

print str(len(Z)) + ' Punkte wurden berechnet.'

eigenvector = np.array([0.5*(gamma-np.sqrt(4+gamma**2)),1])

startpoints = [0.05*eigenvector, 0.05*(-1)*eigenvector]
print startpoints
t2 = np.linspace(0.,20.,1000)
plt.figure(1)
j = 0
colors = ['green', 'cyan']
for startpoint in startpoints:
    wsol = odeint(g,startpoint,t2)
    plt.plot([e[0] for e in wsol],[e[1] for e in wsol],c = colors[j],linewidth = 5, label = 'stable manifold')
    j=j+1

############    PLOTTEN     ####################

XX, YY = np.meshgrid(X,X)

sx = [e[0] for e in startpoints]
sy = [e[1] for e in startpoints]
plt.plot(sx,sy,'o', c = 'black')

C = Z.reshape(N,N)
plt.pcolormesh(XX,YY,C)
plt.title('Gamma = ' + str(gamma))
plt.colorbar()
plt.scatter([-1,1],[0,0],c= 'green',s=50,marker = 'x',edgecolors='green', label = 'Fix points')
plt.legend()
plt.axis([-grid,grid,-grid,grid])
plt.show()
