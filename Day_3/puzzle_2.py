import functools

file = open("input")
base_pattern = [line.strip() for line in file.readlines()]

#Right, Down (j, i)
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
tree_totals = []

for slope in slopes:
	trees = 0
	i = j = 0

	#Count the trees in the way
	while i < len(base_pattern):
		if base_pattern[i%len(base_pattern)][j%len(base_pattern[0])] == "#":
			trees += 1
		j += slope[0]
		i += slope[1]

	tree_totals.append(trees)

print(functools.reduce(lambda a, b:a*b, tree_totals))