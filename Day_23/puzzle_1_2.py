

file=open("input")
cups_aux=[int(i) for i in file.read().strip()]

cups={}

next_label=max(cups_aux)+1

for i in range(len(cups_aux)):
	cups[cups_aux[i]]=[]

keys=list(cups.keys())

for i in range(1, len(cups_aux)-1):
	cups[keys[i]]=[keys[i-1], keys[i+1]]
cups[keys[0]]=[keys[-1], keys[1]]
cups[keys[-1]]=[keys[-2], keys[0]]

#next_cup=3
#for i in range(len(cups)):
#	print(next_cup, end="")
#	next_cup=cups[next_cup][1]
#print()

current=cups_aux[0]

for move in range(100):
	#next_cup=3
	#for i in range(len(cups)):
	#	print(next_cup, end="")
	#	next_cup=cups[next_cup][1]
	#print()

	removed_cups=[]
	#print(cups)
	removed_cups=[cups[current][1], cups[cups[current][1]][1], cups[cups[cups[current][1]][1]][1]]
	cups[current][1]=cups[cups[cups[cups[current][1]][1]][1]][1]
	cups[cups[current][1]][0]=current

	#print("Pick up: ", removed_cups)

	destination=current-1

	while True:
		if destination in removed_cups or destination not in cups:
			if destination-1 < min(cups):
				destination=max(cups)
			else:
				destination-=1
		else:
			break

	#print("Destination: ", destination)
	#print()

	cups[cups[destination][1]][0]=removed_cups[2]

	cups[removed_cups[2]][1]=cups[destination][1]
	cups[removed_cups[2]][0]=removed_cups[1]

	cups[removed_cups[1]][1]=removed_cups[2]
	cups[removed_cups[1]][0]=removed_cups[0]

	cups[removed_cups[0]][1]=removed_cups[1]
	cups[removed_cups[0]][0]=destination

	cups[destination][1]=removed_cups[0]

	current=cups[current][1]

next_cup=3
for i in range(len(cups)):
	print(next_cup, end="")
	next_cup=cups[next_cup][1]
print()