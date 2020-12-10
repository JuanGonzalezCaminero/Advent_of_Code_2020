
def divide_and_conquer(adapters):
	if len(adapters)==1:
		return [[adapters[0]]]
	else:
		combinations_lower=divide_and_conquer(adapters[:int(len(adapters)/2)])
		combinations_upper=divide_and_conquer(adapters[int(len(adapters)/2):])
		#print(combinations_lower, combinations_upper)
		#The number of valid combinations is the number of valid unions 
		#between both halves
		valid_combinations=[]
		for combination_l in combinations_lower:
			for combination_u in combinations_upper:
				#For each pair of combinations, we can check up to 3*3=9 
				#ways of joining them (by removing 0 up to 2 adapters to the right 
				#of the left half and 0 up to 2 to the left of the right half)
				#However, once a certain combination is not valid we dont need 
				#to check what happens if we remove another adapter on that half
				for i in range(min([3, len(combination_l)])):
					lower_length=len(combination_l)
					for j in range(min([3, len(combination_u)])):
						#print(i,j)
						#print(combination_u[j:])
						#print(combination_l[:lower_length-i])
						#If either of the combinations is empty after removing an adapter, add 
						#that as a valid combination as well
						if len(combination_u[j:])==0:
							valid_combinations.append(combination_l[:lower_length-i])
							break
						elif len(combination_l[:lower_length-i])==0:
							valid_combinations.append(combination_u[j:])
							break

						if combination_u[j:][0] - combination_l[:lower_length-i][-1] <= 3:
							if combination_l[:lower_length-i]+combination_u[j:] not in valid_combinations:
								valid_combinations.append(combination_l[:lower_length-i]+combination_u[j:])
						else:
							break

		return valid_combinations



file=open("input")
data=[int(i) for i in file.readlines()]
data.sort()
data.append

print(len(divide_and_conquer(data)))
