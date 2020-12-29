import copy

file=open("input")
state=[]
for i in file.read().strip().split("\n"):
	state.append([[j] for j in i])

#Append borders and 2 dimensions, back and forth
top_bottom=[["."] for i in range(len(state[0]))]
state.insert(0, top_bottom)
state.append(top_bottom)

for i in range(0, len(state)):
	state[i]=[["."]]+state[i]+[["."]]
	for j in range(len(state[i])):
		state[i][j]=["."]+state[i][j]+["."]

print()
for i in state:
	print(i)

state_aux=copy.deepcopy(state)

for step in range(6):
	#first dimension: top, first dimension: bottom,
	#second dimension: left, second dimension: right,
	#third dimension: front, third dimension: back 
	dimensions_to_extend=[0,0,0,0,0,0]

	for i, row in enumerate(state):
		for j, col in enumerate(state[i]):
			for k, cube in enumerate(state[i][j]):
				active_neighbors=0
				for i_aux in range(max([0, i-1]), min([len(state), i+2])):
					for j_aux in range(max([0, j-1]), min([len(state[i_aux]), j+2])):
						for k_aux in range(max([0, k-1]), min([len(state[i_aux][j_aux]), k+2])):

							if i_aux==i and j_aux==j and k_aux==k:
								continue
							else:
								if state[i_aux][j_aux][k_aux]=="#":
									active_neighbors+=1

				if cube=="#":
					if active_neighbors!=2 and active_neighbors!=3:
						state_aux[i][j][k]="."
				else:
					if active_neighbors==3:
						state_aux[i][j][k]="#"
						if i==0:
							dimensions_to_extend[0]=1
						elif i==len(state)-1:
							dimensions_to_extend[1]=1
						if j==0:
							dimensions_to_extend[2]=1
						elif j==len(state[i])-1:
							dimensions_to_extend[3]=1
						if k==0:
							dimensions_to_extend[4]=1
						elif k==len(state[i][j])-1:
							dimensions_to_extend[5]=1

	top_bottom=[["." for j in range(len(state[0][0]))] for i in range(len(state[0]))]

	#print("Step finished")
	#for i in state_aux:
	#	print(i)

	#print("To extend")
	#print(dimensions_to_extend)

	#print()
	#print(top_bottom)
	#print()


	if dimensions_to_extend[0]==1:
		state_aux.insert(0, top_bottom)

	if dimensions_to_extend[1]==1:
		state_aux.append(top_bottom)

	if dimensions_to_extend[2]==1:
		for i in range(len(state_aux)):
			state_aux[i]=[["." for i in range(len(state[0][0]))]]+state_aux[i]

	if dimensions_to_extend[3]==1:
		for i in range(len(state_aux)):
			state_aux[i]=state_aux[i]+[["." for i in range(len(state[0][0]))]]

	if dimensions_to_extend[4]==1:
		for i in range(len(state_aux)):
			for j in range(len(state_aux[i])):
				state_aux[i][j]=["."]+state_aux[i][j]

	if dimensions_to_extend[5]==1:
		for i in range(len(state_aux)):
			for j in range(len(state_aux[i])):
				state_aux[i][j]=state_aux[i][j]+["."]

	state=copy.deepcopy(state_aux)

	#print(step)
	#for i in state:
	#	print(i)


result=0
for i, row in enumerate(state):
	for j, col in enumerate(state[i]):
		for k, cube in enumerate(state[i][j]):
			if cube=="#":
				result+=1

#for i in state:
#	print(i)

print(result)





