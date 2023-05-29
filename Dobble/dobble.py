#n=simbólum kártyánként, r=rekurzió száma

#n-ből kiszámolya a kártyák számát
def Sequence(n,r=0,k=1):
	if n == r:
		return k
	return Sequence(n,r+1,k+(r+1)*2)

#Létrehozza egy paklit az alapján,
#hogy hány szimbólumot szeretnénk kártyánként
def GenerateDeck(n):
	deck = []
	cards = Sequence(n-1)
	symbols = cards
	symbol = 0
	i = 0
	while i < cards:
		deck.append([])	
		i += 1
	while symbol < symbols:
		i = 0
		j = 0
		blacklist = [symbol]
		while i < len(deck) and j < n:
			k = 0
			while k < len(deck[i]) and len(deck[i]) < n and not Van(blacklist,deck[i][k]):
				k += 1
			if k == len(deck[i]):
				for o in deck[i]:
					blacklist.append(o)
				deck[i].append(symbol)
				j +=1
			i += 1
		symbol += 1
	i = 0
	'''
	while i < len(deck):
		if len(deck[i]) != n:
			print('no')
			del deck[i]
		else:
			i += 1'''
	return deck

#Eldönti hogy van-e egy elem egy listában 
def Van(_list,j):
	for i in _list:
		if j == i:
			return True
	return False	

def PrintDeck(deck):
    for i in deck:
        for j in i:
            print(j,end=' ')
        print()

n = int(input("Szimbólum kártyánként(ha 0 akkor atuomatikusan generálni fog növekvő sorrendben): "))
if n == 0:
	i = 1
	while True:
		print()
		print(i,'Simbólum/kártya')
		PrintDeck(GenerateDeck(i))
		i += 1

PrintDeck(GenerateDeck(n))