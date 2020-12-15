import re

file=open("input")

memory={}
mask=["X" for i in range(36)]

for line in file.readlines():
	if re.match("mask", line):
		mask=re.search("[X01]+", line)[0]
	else:
		match=re.findall("[0-9]+", line)
		address=match[0]
		value=list(format(int(match[1]), "036b"))
		for i in range(len(mask)):
			if mask[i]!="X":
				value[i]=mask[i]

		memory[address]=int("".join(value), 2)

result=0
for address in memory:
	result+=memory[address]

print(result)