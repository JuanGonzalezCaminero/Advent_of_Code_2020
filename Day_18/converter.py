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

e="5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
print(e)
#e="1 + 2 + 3"

#print(tokenize(e.replace(" ", "")))
#print(tokenize("(2 + 4 * 9) * (6 + 9 * 8 + 6) + 6".replace(" ", "")))

#print(parenthesize(tokenize(e.replace(" ", ""))))

print(parenthesize_to_string(parenthesize(tokenize(e.replace(" ", "")))))


