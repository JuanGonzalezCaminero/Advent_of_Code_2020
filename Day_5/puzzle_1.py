
import numpy as np

seats=np.zeros([128,8])

file=open("input")

highest_id=0
rows=list(range(128))
cols=list(range(8))

for boarding_pass in file.readlines():
	row=rows
	col=cols
	for char in boarding_pass[:7]:
		if char=="F":
			row=row[:int(len(row)/2)]
		elif char=="B":
			row=row[int(len(row)/2):]
	for char in boarding_pass[7:]:
		if char=="R":
			col=col[int(len(col)/2):]
		elif char=="L":
			col=col[:int(len(col)/2)]
	pass_id=row[0]*8+col[0]
	if pass_id>highest_id:
		highest_id=pass_id

print(highest_id)



