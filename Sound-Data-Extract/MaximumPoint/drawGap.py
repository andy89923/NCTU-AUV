import matplotlib.pyplot as plt
import numpy as np

pre_dir = "./Results/"
ext = ".txt"

def draw(y : [int], nam : int):
	fig = plt.figure()
	ax = fig.subplots()

	ax.plot(np.linspace(0, 1, len(y)), y, 'b.')
	ax.set_title(nam)

	# plt.show()
	plt.savefig(str(nam) + ".png")

def main():
	y = list()
	for deg in range(-90, 91, 30):
		data = open(pre_dir + str(deg) + ext)
		y.clear()

		print("Processing on", deg)
		for i in data:
			if abs(int(i)) > 20:
				continue
			y.append(int(i))


		draw(y, deg)

if __name__ == "__main__":
	main()
