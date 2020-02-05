
import matplotlib.pyplot as plt
import numpy as np

pre_dir = "./data/NewData VOL2/"

num = 0
yy1 = list()
yy2 = list()

data = open(pre_dir + 'dual_0l_pin0.txt')
for i in data:
	now = i.split(',')
	num = num + 1
	# print(float(now[0]), float(now[1]))

	yy1.append(float(now[0]))
	yy2.append(float(now[1]))

	if num >= 333516:
		break


xx = np.linspace(0, 1, num)

print(num)

fig = plt.figure()
ax = fig.subplots()

ax.plot(xx, yy1, 'b')
ax.plot(xx, yy2, 'r')

plt.show()