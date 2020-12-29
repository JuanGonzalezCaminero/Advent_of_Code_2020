import re
import copy

def parenthesize_to_string(expression):
	aux=""
	for i in expression:
		if type(i)==list:
			aux+="("+parenthesize_to_string(i)+") "
		else:
			aux+=i+" "
	aux=aux.replace("( ", "(")
	aux=aux.replace(" )", ")")
	return aux

def parenthesize(expression):
	if type(expression)!=list:
		return expression

	aux=expression

	addition_count=expression.count("+")

	for target_sign in range(addition_count):
		aux=[]
		i=0
		
		while i < len(expression):
			if type(expression[i])==list:
				aux+=[parenthesize(expression[i])]

			elif expression[i]=="+":
				tmp=aux[-1]
				aux=aux[:-1]
				aux.append([tmp, expression[i], parenthesize(expression[i+1])])
				if len(expression)>i+2:
					aux+=expression[i+2:]

				expression=copy.deepcopy(aux)
				break

			else:
				aux.append(expression[i])

			i+=1

	if addition_count==0:
		for i in range(len(aux)):
			if type(aux[i])==list:
				aux[i]=parenthesize(aux[i])

	return aux

def tokenize(expression):
	expression=[i for i in expression]
	aux=[]
	i=0
	while i < len(expression):
		if expression[i]=="(":
			count=0
			parenthesis=[]
			for j in range(i, len(expression)):
				parenthesis+=expression[j]
				if expression[j]=="(":
					count+=1
				elif expression[j]==")":
					count-=1
				if count==0:
					break
				i+=1
			parenthesis=parenthesis[1:-1]
			aux.append(parenthesis)
		else:
			aux.append(expression[i])
		i+=1

	for i in range(len(aux)):
		if type(aux[i])==list:
			aux[i]=tokenize("".join(aux[i]).replace("( ", "(").replace(" )", ")"))

	return aux

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

#e="1 + 2 * 3 + 4 * 5 + 6"
#e="((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

#print(e)
#print(tokenize(e.replace(" ", "")))
#print(parenthesize(tokenize(e.replace(" ", ""))))

#e=parenthesize_to_string(parenthesize(tokenize(e.replace(" ", "")))).strip()
#print(e)

#exp=""
#for i in e[::-1]:
#	if i=="(":
#		exp+=")"
#	elif i==")":
#		exp+="("
#	else:
#		exp+=i

#tree=parse_expression(exp)
#print(evaluate(tree))

#exit()

result=0

#expressions=["1 + 2 * 3 + 4 * 5 + 6",
#"1 + (2 * 3) + (4 * (5 + 6))",
#"2 * 3 + (4 * 5)",
#"5 + (8 * 3 + 9 + 3 * 4 * 3)",
#"5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
#"((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]

for e in expressions:
	print(e)

	e=parenthesize_to_string(parenthesize(tokenize(e.replace(" ", "")))).strip()
	
	print(e)
	print()

	exp=""
	for i in e[::-1]:
		if i=="(":
			exp+=")"
		elif i==")":
			exp+="("
		else:
			exp+=i

	tree=parse_expression(exp)
	#print(evaluate(tree))
	result+=evaluate(tree)

print(result)