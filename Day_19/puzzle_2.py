
import re

#This class should manage different states but since it will be 
#used for executing an automata with a single state, it won't implement that
class PDA():
	def __init__(self, states, alphabet, stack_symbols, transitions, initial_state, initial_stack_symbol):
		self.states=states
		self.alphabet=alphabet
		self.stack_symbols=stack_symbols
		self.transitions=transitions
		self.initial_state=initial_state
		self.stack=[]
		self.initial_stack_symbol=initial_stack_symbol
		self.stack.append(initial_stack_symbol)

	def reset(self):
		self.stack=[self.initial_stack_symbol]

	def run(self, input_chain):
		#Ending condition
		if len(input_chain)==0 and len(self.stack)==0:
			return True
		elif len(input_chain)==0:
			return False
		elif len(self.stack)==0:
			return False
		#Save stack state
		stack_backup=[i for i in self.stack]
		#Explore matching transitions
		for transition in self.transitions:

			if transition[0][2]==self.stack[-1] and (input_chain[0]==transition[0][1] or transition[0][1]=="epsilon"):
				#Pop from stack
				stack_top=self.stack.pop()

				#Add to stack
				if transition[1][1]!="epsilon":
					for i in transition[1][1][::-1]:
						self.stack.append(str(i))

				if transition[0][1]!="epsilon":
					next_input_chain=input_chain[1:]
				else:
					next_input_chain=input_chain

				if self.run(next_input_chain):
					return True
				else:
					#Restore stack
					self.stack=[i for i in stack_backup]

		#If none of the transitions reached an accepting state
		return False


file=open("input_2")
data=file.read().strip().split("\n\n")

rules=data[0].split("\n")
messages=data[1].split("\n")

rules_dict={}
for r in rules:
	rule_index=re.match("[0-9]+", r)[0]
	r=r[len(rule_index)+1:]
	if "a" not in r and "b" not in r:
		rules_dict[rule_index]=[[int(j) for j in i.strip().split(" ")] for i in re.findall("([0-9 ]+)+", r)]
	else:
		rules_dict[rule_index]=[r.strip()[1]]

#Build pushdown automata from the grammar productions
pda_transitions=[]

for variable in rules_dict:
	for alpha in rules_dict[variable]:
		pda_transitions.append([["q", "epsilon", variable], ["q", alpha]])
for terminal in ["a","b"]:
	pda_transitions.append([["q", terminal, terminal], ["q", "epsilon"]])

pda=PDA([], [], [], pda_transitions, "", '0')

result=0
for i in messages:
	if pda.run(i):
		result+=1
	pda.reset()

print(result)



