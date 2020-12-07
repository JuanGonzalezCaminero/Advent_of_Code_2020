import re

file = open("input")
data = file.readlines()

valid_passwords = 0

for password in data:
	policy_number = [int(i) for i in re.search("[0-9]*-[0-9]*", password).group().split("-")]
	policy_letter = re.search("[a-z]:", password).group()[0]
	password_text = re.search(": .*", password).group()[2:]

	if password_text.count(policy_letter) in range(policy_number[0], policy_number[1]+1):
		valid_passwords += 1

print(valid_passwords)