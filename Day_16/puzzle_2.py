
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

valid_tickets=[]

for ticket in tickets:
	valid_ticket=True
	for value in ticket:
		valid=False
		for field in rules:
			for span in rules[field]:
				if value in range(span[0], span[1]+1):
					valid=True
			if valid:
				break
		if not valid:
			valid_ticket=False
			break
	if valid_ticket:
		valid_tickets.append(ticket)

matches={}
for i in rules:
	matches[i]=[0 for j in range(len(rules))]

for ticket in valid_tickets:
	for index, value in enumerate(ticket):
		for field in rules:
			for span in rules[field]:
				if value in range(span[0], span[1]+1):
					valid=True
			if valid:
				matches[field][index]+=1
			valid=False

full_match_count=[matches[i].count(191)-1 for i in matches]

assigned_fields=[]
field_order=[0 for i in range(20)]

for i in range(20):
	key=list(matches.keys())[full_match_count.index(i)]
	for j in assigned_fields:
		matches[key][j]=0
	assigned_fields.append(matches[key].index(191))
	field_order[list(matches.keys()).index(key)]=matches[key].index(191)

print(field_order)

result=1

for i in range(0,6):
	result*=valid_tickets[0][field_order[i]]

print(result)

#for i in range(0,6):
#	print(field_order.index(i))
#	result*=valid_tickets[0][field_order.index(i)]

#print(result)

#result=1

#for i in matches:
#	if "departure" in i:
#		result*=valid_tickets[0][matches[i].count(191)-1]

#print(result)


#3334390970759
#1954811276581

#3765150732757
#958511223419