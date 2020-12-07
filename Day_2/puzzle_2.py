import re

file = open("input")
data = file.readlines()

valid_passwords = 0

for password in data:
	policy_indexes = [int(i) for i in re.search("[0-9]*-[0-9]*", password).group().split("-")]
	policy_letter = re.search("[a-z]:", password).group()[0]
	password_text = re.search(": .*", password).group()[2:]

	#Exclusive OR
	if (password_text[policy_indexes[0]-1]==policy_letter) ^ (password_text[policy_indexes[1]-1]==policy_letter):
		valid_passwords += 1

print(valid_passwords)