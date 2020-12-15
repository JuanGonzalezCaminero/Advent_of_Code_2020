
import re
import math

file=open("input")
data=file.readlines()

#N(+)/S(-)
ship_north_south=0
#E(+)/W(-)
ship_east_west=0
#Waypoint position is relative to the ship
waypoint_north_south=1
waypoint_east_west=10

#Degrees around the ship
angle=math.degrees(math.atan2(-1,10))%360

for instruction in data:
	if instruction[0]=="N":
		waypoint_north_south+=int(instruction[1:])
	elif instruction[0]=="S":
		waypoint_north_south-=int(instruction[1:])
	elif instruction[0]=="E":
		waypoint_east_west+=int(instruction[1:])
	elif instruction[0]=="W":
		waypoint_east_west-=int(instruction[1:])
	elif instruction[0]=="L":
		angle=math.degrees(math.atan2(-waypoint_north_south,waypoint_east_west))%360
		#Modify the angle
		angle-=int(instruction[1:])
		angle=angle%360

		module=math.sqrt(math.pow(waypoint_east_west, 2) + math.pow(waypoint_north_south, 2))
		#print(angle, module)

		waypoint_north_south=-module*math.sin(math.radians(angle))
		waypoint_east_west=module*math.cos(math.radians(angle))
			
	elif instruction[0]=="R":
		angle=math.degrees(math.atan2(-waypoint_north_south,waypoint_east_west))%360
		#Modify the angle
		angle+=int(instruction[1:])
		angle=angle%360

		module=math.sqrt(math.pow(waypoint_east_west, 2) + math.pow(waypoint_north_south, 2))
		#print(angle, module)

		waypoint_north_south=-module*math.sin(math.radians(angle))
		waypoint_east_west=module*math.cos(math.radians(angle))

	elif instruction[0]=="F":
		#y is positive in the lower half of the circle
		ship_north_south+=waypoint_north_south*int(instruction[1:])
		#x is positive in the right half of the circle
		ship_east_west+=waypoint_east_west*int(instruction[1:])

	#print(waypoint_east_west, waypoint_north_south)
	#print(ship_east_west, ship_north_south)
	#print("")

print(abs(ship_north_south) + abs(ship_east_west))