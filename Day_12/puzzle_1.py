import re
import math

file=open("input")
data=file.readlines()

#N(+)/S(-)
north_south=0
#E(+)/W(-)
east_west=0
#Degrees
direction=0

for instruction in data:
	if instruction[0]=="N":
		north_south+=int(instruction[1:])
	elif instruction[0]=="S":
		north_south-=int(instruction[1:])
	elif instruction[0]=="E":
		east_west+=int(instruction[1:])
	elif instruction[0]=="W":
		east_west-=int(instruction[1:])
	elif instruction[0]=="L":
		direction-=int(instruction[1:])
		direction=direction%360
	elif instruction[0]=="R":
		direction+=int(instruction[1:])
		direction=direction%360
	elif instruction[0]=="F":
		#We want to get the (x,y) corresponding
		#to that angle in a unit circle
		x=math.cos(math.radians(direction))
		y=math.sin(math.radians(direction))
		#y is positive in the lower half of the circle
		north_south-=y*int(instruction[1:])
		#x is positive in the right half of the circle
		east_west+=x*int(instruction[1:])

print(abs(north_south) + abs(east_west))