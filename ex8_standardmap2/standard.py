import numpy as np
import matplotlib.pyplot as plt

K = 1
N = 30
iterations = 1000

X,P = np.meshgrid(np.linspace(0,1,N),np.linspace(-1,1,N))

def nextStep(x,p,k):

    xn = (x+p) % 1
    pn = p + k/np.pi/2*np.sin(2*np.pi*xn)

    return xn,pn

def prevStep(x,p,k):
    pn = (p - K/2./np.pi*np.sin(2*np.pi*x))
    xn = (x - pn) % 1
    return xn,pn

plt.figure(1)

for i in range(iterations):
    X, P = nextStep(X, P, K)
    plt.scatter(X, P, marker = ".", s = 0.05, alpha = 1, color = "0.0")

plt.axis([0,1,-.5,.5])

eigenvector1 = np.array([(-np.sqrt(K)+np.sqrt(4+K))/(2*np.sqrt(K)),1])
eigenvector2 = np.array([(-np.sqrt(K)-np.sqrt(4+K))/(2*np.sqrt(K)),1])



startpoints = [0.001*eigenvector1, 0.001*(-1)*eigenvector1,0.001*eigenvector2, 0.001*(-1)*eigenvector2]
print startpoints
color = 0
colors = ['blue', 'red']
for point in [e for e in startpoints if e[0]>0]:
    for i in range(1750):
        plt.scatter(point[0],point[1],marker = "o", s = 5, color = colors[color])
        point[0], point[1] = prevStep(point[0],point[1],K)
        #print prevStep(point[0],point[1],K)
    color += 1
plt.show()
