
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

contain_allergens=[i for i in possible_allergens if i not in cannot_contain]
allergen_identified={}

for i in possible_allergens:
	if i in contain_allergens:
		print(i, possible_allergens[i])


while len(allergen_identified)!=len(contain_allergens):
	for food in contain_allergens:
		if food not in allergen_identified:
			for allergen in possible_allergens[food]:
				identified=True
				amount=possible_allergens[food][allergen]

				#If it has the max appearances of that allergen (and there are no ties)
				if amount==allergens_max[allergen]:
					#Look for ties		
					for food_aux in [i for i in contain_allergens if i!=food]:
						if allergen in possible_allergens[food_aux] and food_aux not in allergen_identified:
							if possible_allergens[food_aux][allergen]==amount:
								identified=False
				else:
					identified=False

				if identified:
					allergen_identified[food]=allergen
					break

for i in allergen_identified:
	print(i, allergen_identified[i])

contain_allergens.sort(key=lambda a:allergen_identified[a])
print(",".join(contain_allergens))







