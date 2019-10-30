

import pylab as plt
import numpy as np

error_threshold = 0.0001
a = -10
b = -9

def f(x):
    ans = x ** 2 - 6 * x + 4
    return ans

fig = plt.figure()
ax = fig.subplots()

fig_x = np.arange(-10.5, 10.5, 0.001)
fig_y = []
fid_x = []
fid_y = []
zeo_y = []

for i in fig_x:
    fig_y.append(f(i))
ax.plot(fig_x, fig_y, 'b')
ax.plot([-10.5, 10.5], [0, 0], 'k')


root = 0
while (b - a > error_threshold):
    fa = f(a)
    fb = f(b)
    x1 = a - ((b - a) * fa / (fb - fa))
    fid_x.append(x1)
    fid_y.append(f(x1))
    zeo_y.append(0)
    a = b
    b = x1
root = b
print(root)

ax.plot(fid_x, fid_y, 'ro')
ax.plot(fid_x, zeo_y, 'bo')

plt.savefig('figure.png')
plt.show()

