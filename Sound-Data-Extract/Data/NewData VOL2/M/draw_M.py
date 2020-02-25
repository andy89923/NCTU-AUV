
import matplotlib.pyplot as plt
import numpy as np

def draw(y1):
	fig = plt.figure()
	ax = fig.subplots()

	ax.plot(np.linspace(0, 1, len(y1)), y1, 'b')
	plt.show()


pre_dir = "./"
ext = ".txt"

num = 0
yy1 = list()

data = open(pre_dir + '30l' + ext)
for i in data:
	yy1.append(float(i))

		
draw(yy1)