
import matplotlib.pyplot as plt
import numpy as np

eps = 0.00000000001
pre_dir = "./Data/NewData VOL2/N_"
ext = "l.txt"
SEQLEN = 9


def draw(y1 : [float], y2 : [float], shi : int):
	fig = plt.figure()
	ax = fig.subplots()

	for i in range(0, shi + 16):
		y2.insert(0, 0.0)

	for i in range(len(y1) - len(y2)):
		y2.append(0.0)

	ax.plot(np.linspace(0, 1, len(y1)), y1, 'b')
	ax.plot(np.linspace(0, 1, len(y1)), y2, 'r')
	ax.set_title(str(shi))

	plt.show()


def proc(y1 : [float], y2 : [float]):
	
	min_shi = 0
	min_sum = 1000

	now_shi = -16
	for i in range(len(y1) - len(y2)):
		now_sum = 0.0
		for j in range(len(y2)):
			if i + j >= len(y1):
				now_sum += y2[j]
			else:
				now_sum += abs(y1[i + j] - y2[j])

		if now_sum < min_sum:
			min_sum = now_sum
			min_shi = now_shi

		now_shi += 1

	# print(now_shi)

	if min_shi <= -12:
		draw(y1, y2, min_shi)

	return min_shi



def calc(y1 : [float], y2 : [float], n : int):
	poi = 0
	cnt = 0
	results = []
	for i in range(n):
		if abs(y2[i]) != 0.0:
			# print("Find first non-zero on", i, y2[i])
			
			results.append(proc(y1[i - SEQLEN*2 : i + SEQLEN*2-1], y2[i - 2 : i + 6]))
			cnt += 1
			i = i + 6
		
	with open('Output.txt', 'w', encoding = 'utf-8') as fout:
		for i in results:
			fout.write(str(i) + "\n")

	return

def main():
	y1 = list()
	y2 = list()

	for deg in range(-90, 90, 30):
		y1.clear()
		y2.clear()
		data = open(pre_dir + str(deg) + ext)
		
		print("Processing on", deg)

		for i in data:
			nums = i.split(',')
			y1.append(float(nums[0]))
			y2.append(float(nums[1]))
		
		calc(y1, y2, len(y1))
		
		break


if __name__ == "__main__":
	main()


	# draw([0.0, 0.0, 0.0,  0.0, 0.0, 0.6,   1.0, 0.5, 0.0,  0.0, 0.0, 0.0], [0.5, 1.0, 0.5], 1)


