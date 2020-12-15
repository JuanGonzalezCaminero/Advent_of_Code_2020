
file=open("input")
seats=[i.strip() for i in file.readlines()]

rows=len(seats)
cols=len(seats[0])
seats=[i for i in "".join(seats)]
seats_aux=[i for i in seats]

layouts={}

while True:
	for i in range(rows):
		for j in range(cols):
			if seats[i*cols + j]==".":
				continue
			occupied=0
			for sub_i in range(i-1, i+2):
				for sub_j in range(j-1, j+2):
					#Move in that direction until a #, L, or the border of 
					#the layout is reached
					sub_i_aux = sub_i
					sub_j_aux = sub_j

					if sub_i!=i or sub_j!=j:
						while sub_i_aux >= 0 and sub_i_aux < rows and sub_j_aux >= 0 and sub_j_aux < cols:
							if seats[sub_i_aux*cols + sub_j_aux]=="#":
								occupied+=1
								break
							elif seats[sub_i_aux*cols + sub_j_aux]=="L":
								break

							sub_i_aux += sub_i-i
							sub_j_aux += sub_j-j


			if occupied==0 and seats[i*cols + j]=="L":
				seats_aux[i*cols + j]="#"
			elif occupied>=5 and seats[i*cols + j]=="#":
				seats_aux[i*cols + j]="L"

	seats=[i for i in seats_aux]

	#for i in range(rows):
	#	print("")
	#	for j in range(cols):
	#		print(seats[i*cols + j], end="")
	#print("")

	if "".join(seats) not in layouts:
		layouts["".join(seats)]=True
	else:
		break

print(seats.count("#"))





