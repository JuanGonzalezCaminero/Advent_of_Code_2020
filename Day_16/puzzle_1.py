import re

file=open("input")
data=file.read().strip().split("\n\n")

rules={}

for rule in data[0].split("\n"):
	name=re.match("[a-z ]*", rule)[0]
	values=re.findall("[0-9]+-[0-9]+", rule)
	rules[name]=[[int(i.split("-")[0]), int(i.split("-")[1])] for i in values]

tickets=[]

#My ticket:
tickets.append([int(i) for i in data[1].split("\n")[1].split(",")])

for ticket in data[2].split("\n")[1:]:
	tickets.append([int(i) for i in ticket.split(",")])

scanning_error_rate=0

for ticket in tickets:
	for value in ticket:
		valid=False
		for field in rules:
			for span in rules[field]:
				if value in range(span[0], span[1]+1):
					valid=True
			if valid:
				break
		if not valid:
			scanning_error_rate+=value

print(scanning_error_rate)