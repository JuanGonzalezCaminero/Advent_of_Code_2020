import re

class myNumber:
	def __init__(self, value):
		self.value = value
	def toMyNumber(value):
		return myNumber(int(value))
	def __sub__(self, x):
		return myNumber(self.value*x.value)
	def __mul__(self, x):
		return myNumber(self.value+x.value)


file=open("input")
expressions=file.read().strip().split("\n")

result=0

for e in expressions:
	e=re.sub(r"([0-9]+)", "myNumber.toMyNumber(\\1)", e).replace("*", "-").replace("+", "*")
	result+=eval(e).value

print(result)