
#a bot által értelmezett szavak listái
positive = ('yes','y','yhea')
negative = ('no','not','n','nothing')
pizzas = (['margareta','margeritha'],['fourcheese','4cheese'],['salami','pepperoni'])
sizes = (['small','kidsize'],['medium','regular'],['large','big'])
extras = (['cheese'],['salami'],['corn'])
drinks = (['cola','kola'],['water'],['tea'])
options = (pizzas,sizes,extras,drinks,drinks)
ordered = [['margeritha','medium','','']]

#a bot által feltett kérdések listái
questions = ('What kind of pizza you would like? ','How big should the pizza be? ','Would you like anythig else on your pizza?','Anything to drink?')
questionsends = ('pizza? ','sized pizza? ','as an extra on your pizza? ','as a drink? ')
optiontypes = ('Pizzas: ','Sizes: ','Extras: ','Drinks: ')

#üdvözlet és menü kiírása
print('Hello! Welcome to our pizza restaurant.')
print('Here is our menu:')
i = 0
while i < len(options)-1:
    print(optiontypes[i],end='')
    for j in options[i]:
        print(j[0],end=' ')
    print()
    i += 1

#az e változó a rendelés fázisát jelenti
#0-pizza
#1-size
#2-extra
#3-drink
#4-anything else
#5-end

#rendelést lebonyolitó ciklus
e = 0
o = 0
while e < 5:
    
    if e == 4:
        request = input('Anything else?')
        o +=1
        
        for i in negative:
            if i == request:
                print(ordered)
                print('Thank you for choosing us!')
                e = 5
                
        #új rendelés felvétele
        if e != 5:
            e = 0
            ordered.append('margeritha','medium','','')
    
    if e == 5:
        break
    
    #éppen aktuális kérdés feltétele és formázása
    request = input(questions[e]).lower().replace(',', '').split(' ')
    
    #a kérés értelmezése
    for i in request:
        j = 0
        while j < len(options[e]):
            k = 0
            while k < len(options[e][j]):
                l = 0
                while l < len(negative):
                    
                    #nemleges e a válasz
                    if i == negative[l]:
                        break
                    
                    elif options[e][j][k] == i:
                        
                        #megerősités
                        comfirmation = input(f'So you want: {i} {questionsends[e]}')
                        for q in comfirmation:
                            
                            for m in positive:
                                #pozitív válasz
                                if q == m:
                                    ordered[o][e] = i
                                    l = len(negative)
                                    k = len(options[e][j])
                                    e += 1
                                else:
                                    #negatív válasz
                                    for p in negative:
                                        if q == p:
                                            l = len(negative)
                                            k = len(options[e][j])
                                            break
                    l += 1
                k += 1
            j += 1
        for n in negative:
            if i == n:
                e = 4
    