
import re

file=open("input")
data=file.read().strip().split("\n\n")
for i in range(len(data)):
	data[i]=data[i].split("\n")

tiles=[]

for tile in data:
	image=tile[1:]
	tile_id=int(re.search("[0-9]+", tile[0])[0])
	left_border="".join([row[0] for row in image])
	right_border="".join([row[-1] for row in image])

	tiles.append([tile_id,[image[0], image[-1], left_border, right_border, \
						   image[0][::-1], image[-1][::-1], left_border[::-1], right_border[::-1]]])

result=1

#The corners will only have two matches
for tile in tiles:
	matches=0
	#Search for matches
	for possible_match in tiles:
		matched=False
		if tile!=possible_match:
			for i in range(8):
				if not matched:
					for j in range(8):
						if tile[1][i]==possible_match[1][j]:
							matches+=1
							matched=True

	if matches==2:
		result*=tile[0]

print(result)




