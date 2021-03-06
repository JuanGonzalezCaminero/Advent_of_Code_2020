

file=open("input")
cups_aux=[int(i) for i in file.read().strip()]

cups={}

next_label=max(cups_aux)+1

for i in range(1000000):
	if i<len(cups_aux):
		cups[cups_aux[i]]=[]
	else:
		cups[next_label]=[]
		next_label+=1

keys=list(cups.keys())

for i in range(1, 1000000-1):
	cups[keys[i]]=[keys[i-1], keys[i+1]]
cups[keys[0]]=[keys[-1], keys[1]]
cups[keys[-1]]=[keys[-2], keys[0]]

current=cups_aux[0]

for move in range(10000000):
	removed_cups=[]
	#print(cups)
	#breakpoint()
	removed_cups=[cups[current][1], cups[cups[current][1]][1], cups[cups[cups[current][1]][1]][1]]
	cups[current][1]=cups[cups[cups[cups[current][1]][1]][1]][1]
	#breakpoint()
	cups[cups[current][1]][0]=current

	#print("Pick up: ", removed_cups)

	destination=current-1

	while True:
		if destination not in cups or destination in removed_cups:
			if destination-1 < 1:
				destination=1000000
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

print(cups[1][1]*cups[cups[1][1]][1])
