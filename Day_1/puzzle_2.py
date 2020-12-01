
import itertools

file = open("input")
data = [int(l) for l in file.readlines()];

for pair in itertools.combinations(data, 3):
	if pair[0]+pair[1]+pair[2] == 2020:
		print("Solution: "+str(pair[0]*pair[1]*pair[2]))