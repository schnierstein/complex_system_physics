import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 1
c = 1
d = 2

x = 3
y = 3

X,Y = np.meshgrid(np.arange(-x,x,0.1),np.arange(-y,y,0.1))

U = a*(1-X)*X-c*X*Y
V = -b*Y+d*X*Y

plt.figure(1)
plt.axis([-x,x,-y,y])

plt.streamplot(X,Y,U,V,density = 4)

#plt.figure(2)
#plt.quiver(X,Y,U,V,pivot = 'mid')#,width = 0.0005)
plt.show()
