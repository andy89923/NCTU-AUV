import matplotlib.pyplot as plt
import numpy as np

pre_dir = "./Results/"
ext = ".txt"

def draw(x : [int], y : [int], nam : int):
	fig = plt.figure()
	ax = fig.subplots()

	ax.barh(x, y)
	ax.set_title(nam)

	# plt.show()
	plt.savefig(str(nam) + "_bar.png")


def main():
	x = list()
	y = list()
	for i in range(-15, 16, 1):
		x.append(i)

	for deg in range(-90, 91, 30):
		data = open(pre_dir + str(deg) + ext)

		y.clear()
		for i in range(len(x)):
			y.append(0)

		print("Processing on", deg)
		for i in data:
			if abs(int(i)) > 15:
				continue
			y[int(i) + 15] += 1

		draw(x, y, deg)

if __name__ == "__main__":
	main()
