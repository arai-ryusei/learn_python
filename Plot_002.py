
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(331)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(332)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.subplot(333)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(334)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.subplot(337)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.show()


plt.figure(2)
x1 = np.arange(0.0, 5.0, 0.1)
x2 = np.arange(0.0, 5.0, 0.1)
y1 = np.arange(0.0, 5.0, 0.1)
y2 = np.arange(0.0, 5.0, 0.1)

lines = plt.plot(x1, y1, x2, y2)
# 飾り
plt.setp(lines, color='r', linewidth=2.0)
plt.show()



