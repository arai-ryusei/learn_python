# MatPlot_002.py

import random
import numpy as np
import matplotlib.pyplot as plt

y0 = np.random.randn(100000)
x = np.linspace(-5.0, 5.0, 100)

y = []
for kk in range(0,99):
	x1 = x[kk];  x2 = x[kk+1]
	n = 0
	for xx in y0:
		if x1 <= xx and xx < x2:
			n = n + 1
	y.append(n)

y.append(0.0)
plt.plot(x, y, '+')
plt.show()


