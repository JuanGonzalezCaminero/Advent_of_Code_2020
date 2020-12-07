import numpy as np

file=open("input")
data=file.read().strip()
data=data.split("\n\n")
for i in range(len(data)):
	data[i]=data[i].replace("\n", "")
	data[i]=[c for c in data[i]]

yes_answers=0

for group in data:
	yes_answers+=len(np.unique(group))

print(yes_answers)