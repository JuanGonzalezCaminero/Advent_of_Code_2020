
file=open("input")
numbers=[int(i) for i in file.read().strip().split(",")]

turn=len(numbers)

while turn<2020:
	if numbers[-1] in numbers[:-1]:
		#Get all indices for the repeated number
		indices=[index+1 for index, value in enumerate(numbers) if value==numbers[-1]]
		next_number=indices[-1]-indices[-2]
	else:
		next_number=0
	#print(next_number)
	numbers.append(next_number)
	turn+=1

print(numbers[-1])