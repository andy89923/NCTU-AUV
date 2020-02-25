
import matplotlib.pyplot as plt
import numpy as np

def draw(y1, y2):
	fig = plt.figure()
	ax = fig.subplots()

	ax.plot(np.linspace(0, 1, len(yy1)), yy1, 'b')
	ax.plot(np.linspace(0, 1, len(yy2)), yy2, 'r')

	plt.show()

pre_dir = "./Data/NewData VOL2/"
ext = ".txt"

num = 0
yy1 = list()
yy2 = list()

data = open(pre_dir + 'N_30l' + ext)
for i in data:
	now = i.split(',')
	num = num + 1
	# print(float(now[0]), float(now[1]))

	yy1.append(float(now[0]))
	yy2.append(float(now[1]))

		
draw(yy1, yy2)