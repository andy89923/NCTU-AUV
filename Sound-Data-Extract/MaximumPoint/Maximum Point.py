
import matplotlib.pyplot as plt
import numpy as np

def draw(y1, y2):
	fig = plt.figure()
	ax = fig.subplots()

	ax.plot(np.linspace(0, 1, len(yy1)), yy1, 'b')
	ax.plot(np.linspace(0, 1, len(yy2)), yy2, 'r')

	plt.show()

def getMax(lis):
	poi = -1
	num = 0
	for i in range(len(lis)):
		if lis[i] > num:
			num = lis[i]
			poi = i
	return poi


pre_dir = "./data/NewData VOL2/"

num = 0
yy1 = list()
yy2 = list()

data = open(pre_dir + 'dual_-90l_pin0.txt')
for i in data:
	now = i.split(',')
	num = num + 1
	# print(float(now[0]), float(now[1]))

	yy1.append(float(now[0]))
	yy2.append(float(now[1]))

	if num >= 303516:
		poi1 = getMax(yy1)
		poi2 = getMax(yy2)

		print(poi1, poi2, poi2 - poi1)
		draw(yy1, yy2)
		
		num = 0
		yy1.clear()
		yy2.clear()

