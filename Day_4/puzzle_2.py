import re

file=open("input")
data=file.read().strip()
data=data.split("\n\n")
for i in range(len(data)):
	data[i]=data[i].replace("\n", " ")

documents=[]

for line in data:
	elements=line.split(" ")
	new_document={}
	for element in elements:
		element=element.split(":")
		new_document[element[0]]=element[1]
	documents.append(new_document)

valid_passports=0

for document in documents:
	if "byr" in document and\
		"iyr" in document and\
		"eyr" in document and\
		"hgt" in document and\
		"hcl" in document and\
		"ecl" in document and\
		"pid" in document and\
		int(document["byr"]) >= 1920 and\
		int(document["byr"]) <= 2002 and\
		int(document["iyr"]) >= 2010 and\
		int(document["iyr"]) <= 2020 and\
		int(document["eyr"]) >= 2020 and\
		int(document["eyr"]) <= 2030 and\
		((document["hgt"][-2:]=="cm" and\
		int(document["hgt"][:-2]) >= 150 and\
		int(document["hgt"][:-2]) <= 193) !=\
		(document["hgt"][-2:]=="in" and\
		int(document["hgt"][:-2]) >= 59 and\
		int(document["hgt"][:-2]) <= 76)) and\
		re.match("#[0-9a-f]{6}", document["hcl"]) != None and\
		len(document["hcl"]) == 7 and\
		re.match("amb|blu|brn|gry|grn|hzl|oth", document["ecl"]) != None and\
		re.match("[0-9]{9}", document["pid"]) != None and\
		len(document["pid"]) == 9:
		valid_passports+=1

print(valid_passports)
