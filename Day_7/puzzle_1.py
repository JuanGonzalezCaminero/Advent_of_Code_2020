import re

def dict_dfs(dic, color):
	if color == "shiny gold":
		return True
	else:
		for bag in dic[color]:
			if dict_dfs(dic, re.search("[a-z]+ [a-z]+", bag)[0]):
				return True

file = open("input")
bag_descriptions={}

for bag in file.readlines():
	color = re.match("[a-z]* [a-z]*", bag)[0]
	contents = re.findall("[0-9]+ [a-z]+ [a-z]+", bag)
	bag_descriptions[color]=contents

can_contain = 0

for bag in bag_descriptions:
	if dict_dfs(bag_descriptions, bag) and bag!="shiny gold":
		can_contain+=1

print(can_contain)