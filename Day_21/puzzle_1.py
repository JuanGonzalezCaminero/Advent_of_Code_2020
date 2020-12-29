import re

file=open("input")

foods=[]

for i in file.readlines():
	ingredients=re.match("[^(]*", i)[0].strip().split(" ")
	allergens=re.search("\(.*\)", i)[0][10:-1].split(", ")
	foods.append([ingredients, allergens])

possible_allergens={}
allergens_max={}

for food in foods:
	for ingredient in food[0]:
		if ingredient not in possible_allergens:
			possible_allergens[ingredient]={}
		for allergen in food[1]:
			if allergen not in possible_allergens[ingredient]:
				possible_allergens[ingredient][allergen]=1
			else:
				possible_allergens[ingredient][allergen]+=1
			if allergen not in allergens_max:
				allergens_max[allergen]=1
			else:
				if allergens_max[allergen]<possible_allergens[ingredient][allergen]:
					allergens_max[allergen]=possible_allergens[ingredient][allergen]

cannot_contain=[]

for food in possible_allergens:
	cant=True
	for allergen in possible_allergens[food]:
		if possible_allergens[food][allergen]>=allergens_max[allergen]:
			cant=False
			break

	if cant:
		cannot_contain.append(food)

result=0
for food in foods:
	for safe_ingredient in cannot_contain:
		if safe_ingredient in food[0]:
			result+=1
print(result)



