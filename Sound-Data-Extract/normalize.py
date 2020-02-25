from sklearn import preprocessing
import numpy as np

pre_dir = "./data/NewData VOL2/"
ext = ".txt"

def Normalize(filename):
	X = []
	Y = []
	with open(filename, 'r', encoding='utf-8') as fin:
		for row in fin:
			row = row.split(",")
			X.append(float(row[0]))
			Y.append(float(row[1][:-1]))
	
	X = np.array(X)
	Y = np.array(Y)

	Xn = X / np.linalg.norm(X)
	Yn = Y / np.linalg.norm(Y)

	return Xn, Yn

def Run(filenames):
	for f in filenames:
		print("Processing on '" + f + "'")

		Xn, Yn = Normalize(pre_dir + f + ext)

		with open(pre_dir + "N_" + f + ext, 'w', encoding = 'utf-8') as fout:
			for i in range(len(Xn)):
				fout.write(str(Xn[i]) + "," + str(Yn[i]) + "\n")


lis = list()
for i in range(-90, 91, 30):
	ss = str(i) + 'l'
	lis.append(str(i) + "l")

# print(lis)
Run(['-90l'])
# Run(lis)