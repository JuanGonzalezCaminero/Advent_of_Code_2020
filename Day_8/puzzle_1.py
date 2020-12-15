

def parse_code(text_code):
	code=[]
	for instruction in text_code.split("\n"):
		operation, argument = instruction.split(" ")
		code.append([operation, int(argument)])
	return code

def execute_code(code):
	#Only for day 8:
	executed_instructions=[]
	accumulator=0

	program_counter=0
	while(True):
		#Only for day 8
		if program_counter in executed_instructions:
			print(accumulator)
			break
		executed_instructions.append(program_counter)

		operation, argument=code[program_counter]
		if operation == "acc":
			accumulator+=argument
			program_counter+=1
		elif operation == "jmp":
			program_counter+=argument
		elif operation == "nop":
			program_counter+=1
		


file=open("input")
data=file.read().strip()
execute_code(parse_code(data))




