# MatPlot_001.py

import random
import numpy as np
import matplotlib.pyplot as plt



x = np.arange(0., 100., 0.1)
print(x.shape)
y=[]

for element in x:
	y.append( random.randrange(100) )
	#print(y)

print(y)
#plt.grid(True)
plt.plot(x, y, 'ro' )
plt.show()


