import numpy as np
import matplotlib.pyplot as plt

K = 1
N = 30
iterations = 1000

X,P = np.meshgrid(np.linspace(0,1,N),np.linspace(-1,1,N))

def nextStep(x,p,k):

    xn = (x+p)%1
    pn = p + k/np.pi/2*np.sin(2*np.pi*xn)

    return xn,pn

plt.figure(1)

for i in range(iterations):
    X, P = nextStep(X, P, K)
    plt.scatter(X, P, marker = ".", s = 0.05, alpha = 1, color = "0.0")

plt.axis([0,1,-1.5,1.5])
plt.show()
