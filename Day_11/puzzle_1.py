
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
			for sub_i in range(max([0,i-1]), min([rows, i+2])):
				for sub_j in range(max([0,j-1]), min([cols, j+2])):
					if seats[sub_i*cols + sub_j]=="#":
						if sub_i!=i or sub_j!=j:
							occupied+=1
			if occupied==0 and seats[i*cols + j]=="L":
				seats_aux[i*cols + j]="#"
			elif occupied>=4 and seats[i*cols + j]=="#":
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





