
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
		"pid" in document:
		valid_passports+=1

print(valid_passports)
