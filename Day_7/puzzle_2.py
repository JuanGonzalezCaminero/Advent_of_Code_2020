import re

def dict_dfs_count(dic, color, number):
	count=0
	if len(dic[color]) == 0:
		return number
	for bag in dic[color]:
		count += dict_dfs_count(dic, re.search("[a-z]+ [a-z]+", bag)[0], int(re.match("[0-9]+", bag)[0])) * number
	return count+number

file = open("input")
bag_descriptions={}

for bag in file.readlines():
	color = re.match("[a-z]* [a-z]*", bag)[0]
	contents = re.findall("[0-9]+ [a-z]+ [a-z]+", bag)
	bag_descriptions[color]=contents

count = dict_dfs_count(bag_descriptions, "shiny gold", 1)
print(count-1)