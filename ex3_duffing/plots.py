import numpy as np
import matplotlib.pyplot as plt

p = 3.
b = 2.

x = 2
y = 2
gamma = 3.

points= [[p/2.-b/2.,0],[1,p/b]]

X,Y = np.meshgrid(np.arange(-x,x,0.2),np.arange(-y,y,0.2))

U = Y
V = -gamma*Y+X-X**3

plt.figure(1)
plt.axis([-x,x,-y,y])

plt.streamplot(X,Y,U,V,density=3)
w,z = points
plt.plot(w,z,'x')
plt.figure(2)
plt.quiver(X,Y,U,V,pivot = 'mid')#,width = 0.0005)
plt.show()
