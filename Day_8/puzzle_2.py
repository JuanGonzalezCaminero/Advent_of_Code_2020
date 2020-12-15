
def parse_code(text_code):
	code=[]
	for instruction in text_code.split("\n"):
		operation, argument = instruction.split(" ")
		code.append([operation, int(argument)])
	return code

def execute_code(code):
	#Only for day 8:
	accumulator=0
	executed_instructions=[]

	program_counter=0
	while(True):
		#Only for day 8
		if program_counter in executed_instructions:
			return False
		executed_instructions.append(program_counter)

		#Finishing condition:
		if program_counter == len(code):
			break

		operation, argument=code[program_counter]
		if operation == "acc":
			accumulator+=argument
			program_counter+=1
		elif operation == "jmp":
			program_counter+=argument
		elif operation == "nop":
			program_counter+=1

	#Only for day 8
	print("Success: " + str(accumulator))
	return True

file=open("input")
data=file.read().strip()

code=parse_code(data)

for instruction in range(len(code)):
	previous_value=code[instruction][0]
	if code[instruction][0]=="jmp":
		code[instruction][0]="nop"
	elif code[instruction][0]=="nop":
		code[instruction][0]="jmp"

	if execute_code(code):
		break

	code[instruction][0]=previous_value