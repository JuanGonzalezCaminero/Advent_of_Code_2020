
file=open("input")
data=[int(i) for i in file.read().strip().split(",")]
turn=len(data)

numbers={}
for i in data:
	numbers[i]=data.index(i)+1

last_number=data[-1]

while turn<30000000:
	if last_number in numbers:
		next_number=turn - numbers[last_number]
		numbers[last_number]=turn
	else:
		next_number=0
		numbers[last_number]=turn
	#print(next_number)
	last_number=next_number
	turn+=1

print(last_number)