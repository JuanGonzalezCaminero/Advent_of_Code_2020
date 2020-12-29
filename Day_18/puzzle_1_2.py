import re

class myNumber:
	def __init__(self, value):
		self.value = value
	def toMyNumber(value):
		return myNumber(int(value))
	def __sub__(self, x):
		return myNumber(self.value*x.value)
	def __add__(self, x):
		return myNumber(self.value+x.value)


file=open("input")
expressions=file.read().strip().split("\n")

result=0

#expressions=["1 + 2 * 3 + 4 * 5 + 6",
#"1 + (2 * 3) + (4 * (5 + 6))",
#"2 * 3 + (4 * 5)",
#"5 + (8 * 3 + 9 + 3 * 4 * 3)",
#"5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
#"((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]

for e in expressions:
	#print(re.search("[0-9]+", e))
	e=re.sub(r"([0-9]+)", "myNumber.toMyNumber(\\1)", e).replace("*", "-")
	#print(e)
	#print(eval(e).value)
	result+=eval(e).value

print(result)