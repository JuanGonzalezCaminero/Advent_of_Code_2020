
file=open("input")
data=[int(i) for i in file.readlines()]
data.sort()

current_joltage=0
differences=[0,0,0]

for adapter in data:
	differences[adapter-current_joltage-1]+=1
	current_joltage=adapter

#Device adapter (3 jolt difference)
differences[2]+=1
current_joltage+=3

print(differences)
print(differences[0]*differences[2])