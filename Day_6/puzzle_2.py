import numpy as np

file=open("input")
data=file.read().strip()
data=data.split("\n\n")

yes_answers=0

for grp in range(len(data)):
	group_members=len(data[grp].split("\n"))
	group=data[grp].replace("\n", "")
	group=[c for c in group]
	for yes in np.unique(group):
		if group.count(yes)==group_members:
			yes_answers+=1
			
print(yes_answers)