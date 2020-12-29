import re

def evaluate(node):
	if len(node)==1:
		return int(node[0])

	if node[1]=="+":
		return evaluate(node[0]) + evaluate(node[2])
	elif node[1]=="-":
		return evaluate(node[0]) - evaluate(node[2])
	elif node[1]=="*":
		return evaluate(node[0]) * evaluate(node[2])
	elif node[1]=="/":
		return evaluate(node[0]) / evaluate(node[2])


def parse_expression(expression):
	#exp=re.match(r"(?P<operand>[0-9]+|\(.*\)) (?P<operator>\+|-|\*|/) (?P<rest>.*)", expression)
	#print(exp.groupdict())
	if not any(i in expression for i in ["+", "-", "*", "/"]):
		return expression

	components={}
	#operand=""
	if expression[0]=="(":
		opening=0
		for i, val in enumerate(expression):
			if val=="(":
				opening+=1
			elif val==")":
				opening-=1
			if opening==0:
				operand=expression[1:i]
				expression=expression[i+1:]
				break

		if expression!="":
			exp=re.match(r" (?P<operator>\+|-|\*|/) (?P<rest>.*)", expression)
			components=exp.groupdict()
			components["operand"]=parse_expression(operand)
		else:
			return parse_expression(operand)

	else:
		exp=re.match(r"(?P<operand>[0-9]+) (?P<operator>\+|-|\*|/) (?P<rest>.*)", expression)
		components=exp.groupdict()

	return[components["operand"], components["operator"], parse_expression(components["rest"])]


file=open("input")
expressions=file.read().strip().split("\n")

#e="(1 + 2) * 3 + 4 * 5 + 6"
#e="((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

result=0

for e in expressions:
	exp=""
	for i in e[::-1]:
		if i=="(":
			exp+=")"
		elif i==")":
			exp+="("
		else:
			exp+=i

	tree=parse_expression(exp)
	result+=evaluate(tree)

print(result)

#print(tree)
#print(evaluate(tree))


