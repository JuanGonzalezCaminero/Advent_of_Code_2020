
file = open("input")
base_pattern = [line.strip() for line in file.readlines()]

#Right, Down (j, i)
slope = (3,1)

trees = 0
i = j = 0

#Count the trees in the way
while i < len(base_pattern):
	if base_pattern[i%len(base_pattern)][j%len(base_pattern[0])] == "#":
		trees += 1
	j += slope[0]
	i += slope[1]

print(trees)