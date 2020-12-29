
import copy

file=open("input")
state=[]
for i in file.read().strip().split("\n"):
	state.append([[[j]] for j in i])

#for i in state:
#	print(i)

state_aux=copy.deepcopy(state)

for i in range(7):
	top_bottom=[[["." for k in range(len(state[0][0][0]))] for j in range(len(state[0][0]))] for i in range(len(state[0]))]
	state_aux.insert(0, top_bottom)
	state_aux.append(top_bottom)

	for i in range(len(state_aux)):
		state_aux[i]=[[["." for k in range(len(state[0][0][0]))] for j in range(len(state[0][0]))]]+state_aux[i]+[[["." for k in range(len(state[0][0][0]))] for j in range(len(state[0][0]))]]

		for j in range(len(state_aux[i])):
			state_aux[i][j]=[["." for k in range(len(state[0][0][0]))]]+state_aux[i][j]+[["." for k in range(len(state[0][0][0]))]]

			for k in range(len(state_aux[i][j])):
				state_aux[i][j][k]=["."]+state_aux[i][j][k]+["."]

	state=copy.deepcopy(state_aux)

#for i in state:
#	print(i)
#print()
#print()


state_aux=copy.deepcopy(state)

for step in range(6):

	for i, row in enumerate(state):
		for j, col in enumerate(state[i]):
			for k, plane in enumerate(state[i][j]):
				for w, cube in enumerate(state[i][j][k]):
					active_neighbors=0
					for i_aux in range(max([0, i-1]), min([len(state), i+2])):
						for j_aux in range(max([0, j-1]), min([len(state[i_aux]), j+2])):
							for k_aux in range(max([0, k-1]), min([len(state[i_aux][j_aux]), k+2])):
								for w_aux in range(max([0, w-1]), min([len(state[i_aux][j_aux][k_aux]), w+2])):

									if i_aux==i and j_aux==j and k_aux==k and w_aux==w:
										continue
									else:
										if state[i_aux][j_aux][k_aux][w_aux]=="#":
											active_neighbors+=1

					if cube=="#":
						if active_neighbors!=2 and active_neighbors!=3:
							state_aux[i][j][k][w]="."
					else:
						if active_neighbors==3:
							state_aux[i][j][k][w]="#"

	state=copy.deepcopy(state_aux)

	#print(step)
	#for i in state:
	#	print(i)


result=0
for i, row in enumerate(state):
	for j, col in enumerate(state[i]):
		for k, plane in enumerate(state[i][j]):
			for w, cube in enumerate(state[i][j][k]):
				if cube=="#":
					result+=1

#for i in state:
#	print(i)

print(result)





