import itertools

file=open("input")
data=[int(i) for i in file.read().strip().split("\n")]

previous_25=data[:25]

for i in range(25, len(data)):
	number=data[i]
	compliant=False
	for pair in itertools.combinations(data, 2):
		if number == pair[0]+pair[1]:
			compliant=True
	if not compliant:
		print(number)
		exit()


