
file=open("input")
adapters=[int(i) for i in file.readlines()]+[0]
adapters.sort()

#print(adapters)

#Connections list, row- adapter, column, adapters it can connect to
connections=[[] for i in range(len(adapters))]

#A node can be connected, at most, with the node 3 positions to its right
#Register connections only in one direction
for adapter in range(len(adapters)):
	for i in range(adapter+1, min([adapter+4, len(adapters)])):
		if adapters[i]-adapters[adapter] <= 3:
			connections[adapter].append(i)

#print(connections)

num_routes=[0 for i in range(len(adapters))]
num_routes[-1]=1

for adapter in range(len(adapters)-1, -1, -1):
	for exit in connections[adapter]:
		num_routes[adapter]+=num_routes[exit]

#print(num_routes)

print(num_routes[0])






