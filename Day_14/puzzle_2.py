
import re

def find_addresses(address):
	addresses=[]
	for i in range(len(address)):
		if address[i]=="X":
			address[i]='0'
			addresses+=find_addresses([i for i in address])
			address[i]='1'
			addresses+=find_addresses([i for i in address])
			return addresses
	return [[i for i in address]]


file=open("input")

memory={}
mask=["X" for i in range(36)]

for line in file.readlines():
	if re.match("mask", line):
		mask=re.search("[X01]+", line)[0]
	else:
		match=re.findall("[0-9]+", line)
		address=list(format(int(match[0]), "036b"))
		value=int(match[1])

		for i in range(len(mask)):
			if mask[i]!="0":
				address[i]=mask[i]

		addresses=find_addresses([i for i in address])

		for a in addresses:
			memory["".join(a)]=value

result=0
for address in memory:
	result+=memory[address]

print(result)