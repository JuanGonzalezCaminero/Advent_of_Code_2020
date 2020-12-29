
file=open("input")
tiles_to_flip=file.read().strip().split("\n")

flip_count={}

for tile in tiles_to_flip:
	if tile in flip_count:
		flip_count[tile]+=1
	else:
		flip_count[tile]=1

result=0
for tile in flip_count:
	if flip_count[tile]%2!=0:
		result+=1
print(result)