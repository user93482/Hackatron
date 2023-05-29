import random

#Létrehozza a pályát és a pitont
def GenerateMap(width,height):
	Map = []
	height += 2
	for i in range(height):
		Map.append(['*'])
		for j in range(width):
			if i == 0 or i == height-1:
				Map[i].append('*')
			else:
				Map[i].append(' ')
		Map[i].append('*')
	cordy = random.randint(1,height-2)
	cordx = random.randint(1,width)
	Map[cordy][cordx] = '@'
	return Map,cordy,cordx 

#Kiirja a pályát
def PrintMap(Map):
	for i in Map:
		print()
		for j in i:
			print(j,end='')
	print()

#A felhasználó parancsait fogadja, dolgozza fel és reagál rá
def Commands(Map):
	cordy = Map[1]
	cordx = Map[2]
	Map = Map[0]
	commands = {'balra':[0,-1],'jobbra':[0,1],'fel':[-1,0],'le':[1,0]}
	PrintMap(Map)
	while True:
		command = input('Hova?')	
		if command == 'meguntam':
			break
		elif van(commands,command):
			if Map[cordy+commands[command][0]][cordx+commands[command][1]] == '*':
				break
			Map[cordy][cordx] = ' '
			cordy += commands[command][0]
			cordx += commands[command][1]
			Map[cordy][cordx] = '@'
			PrintMap(Map)
		else:
			print('Nem értettem')
	print('Most ennyi volt, szép napot!')
	return [Map,cordy,cordx]

#Eldönti hogy van-e egy elem egy listában 
def van(_list,j):
	for i in _list:
		if j == i:
			return True
	return False	

width = 60 #pálya szélessége
height = 30#pálya magassága

Map = GenerateMap(width,height)

Commands(Map)