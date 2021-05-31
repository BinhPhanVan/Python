import numpy as np
import matplotlib.pyplot as plt
x= np.arange(0,3*np.pi,0.1)
y= np.sin(x)
y_cos = np.cos(x)
y_sin = np.sin(x)
plt.subplot(2,1,1)
plt.plot(y_cos)
plt.subplot(2,1,2)
plt.plot(y_sin)
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.show()
 