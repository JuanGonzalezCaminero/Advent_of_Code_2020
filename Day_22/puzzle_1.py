
file=open("input")
player_decks=[[int(j) for j in i.strip().split("\n")[1:]] for i in file.read().split("\n\n")]

while len(player_decks[0])!=0 and len(player_decks[1])!=0:
	card0=player_decks[0].pop(0)
	card1=player_decks[1].pop(0)
	if card0>card1:
		player_decks[0].append(card0)
		player_decks[0].append(card1)
	else:
		player_decks[1].append(card1)
		player_decks[1].append(card0)

result=0
if len(player_decks[0])!=0:
	for i, val in enumerate(player_decks[0][::-1]):
		result+=(i+1)*val
else:
	for i, val in enumerate(player_decks[1][::-1]):
		result+=(i+1)*val

print(result)



