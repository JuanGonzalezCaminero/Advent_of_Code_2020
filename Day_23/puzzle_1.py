
file=open("input")
cups=[int(i) for i in file.read().strip()]

current_cup_label=cups[0]

for move in range(100):
	#print(cups)
	removed_cups=[]

	for i in range(3):
		removed_cups.append(cups.pop((cups.index(current_cup_label)+1)%len(cups)))

	#print("Pick up: ", removed_cups)

	destination=current_cup_label-1

	while True:
		if destination not in cups:
			if destination-1 < min(cups):
				destination=max(cups)
			else:
				destination-=1
		else:
			break

	#print("Destination: ", destination)
	#print()

	destination_index=cups.index(destination)%len(cups)
	for i in range(3):
		cups.insert(destination_index+1, removed_cups.pop(-1))
		#destination_index+=1

	current_cup_label=cups[(cups.index(current_cup_label)+1)%len(cups)]

result=[]
current_index=(cups.index(1)+1)%len(cups)
for i in range(len(cups)-1):
	result.append(cups[current_index])
	current_index=(current_index+1)%len(cups)

print(int("".join([str(i) for i in result])))









