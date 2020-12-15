#import numpy as np
import math

file=open("input")
data=file.read()

earliest=int(data.split("\n")[0])
buses=[int(i) for i in data.split("\n")[1].split(",") if i != "x"]
#Lowest common multiple of the buses
#lcm=np.lcm.reduce(buses)

print(earliest)
print(buses)
#print(lcm)

#Timestamps at wich each bus will arrive after our earliest arrival
timestamps=[math.ceil(earliest/i)*i for i in buses]

print((min(timestamps)-earliest)*buses[timestamps.index(min(timestamps))])
