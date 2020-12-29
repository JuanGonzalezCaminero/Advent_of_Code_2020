
def play(deck_0, deck_1):
	already_played=[]
	
	while len(deck_0)!=0 and len(deck_1)!=0:
		if deck_0 in [i[0] for i in already_played] and deck_1 in [i[1] for i in already_played]:
			return 0

		already_played.append([[i for i in deck_0], [i for i in deck_1]])
		card0=deck_0.pop(0)
		card1=deck_1.pop(0)
		if len(deck_0)>=card0 and len(deck_1)>=card1:
			winner=play([i for i in deck_0[:card0]], [i for i in deck_1[:card1]])
		else:
			if card0>card1:
				winner=0
			else:
				winner=1
		if winner==0:
			deck_0.append(card0)
			deck_0.append(card1)
		else:
			deck_1.append(card1)
			deck_1.append(card0)

	if len(deck_0)!=0:
		return 0
	else:
		return 1


file=open("input")
player_decks=[[int(j) for j in i.strip().split("\n")[1:]] for i in file.read().split("\n\n")]

play(player_decks[0], player_decks[1])

result=0
if len(player_decks[0])!=0:
	for i, val in enumerate(player_decks[0][::-1]):
		result+=(i+1)*val
else:
	for i, val in enumerate(player_decks[1][::-1]):
		result+=(i+1)*val

print(result)




