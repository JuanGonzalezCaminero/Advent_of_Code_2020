def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    
    while r != 0:
    	q = old_r//r
    	old_r, r = r, old_r-q*r
    	old_s, s = s, old_s-q*s
    	old_t, t = t, old_t-q*t

    return old_s

    #output "Bézout coefficients:", (old_s, old_t)
    #output "greatest common divisor:", old_r
    #output "quotients by the gcd:", (t, s)

file=open("input")
data=file.read().split("\n")[1].split(",")

buses=[int(i) for i in data if i != "x"]
offsets=[data.index(i) for i in data if i != "x"]

print(buses)
print(offsets)

for bus in buses:
	print("t="+str(-1*offsets[buses.index(bus)])+" mod("+str(bus)+")")

N=1
for bus in buses:
	N*=bus

print(N)

sol=0

for bus in range(len(buses)):
	s = extended_gcd( N//buses[bus], buses[bus])
	sol+= (-1*offsets[bus]*s*N)//buses[bus]

print(sol)
print(sol%N)

#Earliest
#100000000000000
#Will happen before lcm:
#1182259336403743
#Will happen at a multiple of the first bus id:
#cycle*29 = timestamp
#For each pair offset, id:
#cycle*id = timestamp+offset
