from turtle import circle, forward, left, right, exitonclick, speed, penup, pendown, goto, color, pensize

ctverec = 50
while(True):
    radek = (input('Zadej počet řádků:'))
    if not radek.isnumeric():
        print("Zkus to znovu a zadej celé kladné číslo")
        continue

    radek = int(radek)
    if(radek == 0):
        print("Zkus to znovu a zadej célé kladné číslo")
    else:
        break

while(True):
    sloupec = (input('Zadej počet sloupců:'))
    if not sloupec.isnumeric():
        print("Zkus to znovu a zadej celé kladné číslo")
        continue

    sloupec = int(sloupec)
    if(sloupec == 0):
        print("Zkus to znovu a zadej célé kladné číslo")
    else:
        break

speed(0)
pensize (3)
for _ in range(radek):
    for _ in range(sloupec):
        for _ in range(4):
            forward(ctverec)
            left(90)
        forward(ctverec)
    left(180)
    forward(sloupec*ctverec)
    right(90)
    forward(ctverec)
    right(90)


hrac = True

for _ in range(sloupec*radek):
    if(hrac):
        print("Hraje hráč X")
    else:
        print("Hraje hráč O")
    while(True):
        x = input("Zadej souřadnici x: ")
        if not x.isnumeric():
            print("Zkus to znovu a zadej číslo")
            continue

        x = int(x)
        if(x <= 0 or x > sloupec):
            print("Zkus to znovu ")
        else:
            break

    while(True):
        y = input("Zadej souřadnici y: ")
        if not y.isnumeric():
            print("Zkus to znovu")
            continue

        y = int(y)
        if(y <= 0 or y > radek):
            print("Zkus to znovu ")
        else:
            break
    
    poziceX = (x-1)*ctverec
    poziceY = (radek+1-y)*ctverec
    
    if hrac: 
        color('blue')
        penup()
        goto(poziceX, poziceY)
        pendown()
        goto(poziceX+ctverec, poziceY-ctverec)
        penup()
        goto(poziceX+ctverec, poziceY)
        pendown()
        goto(poziceX, poziceY-ctverec)
    else:
        color('red')
        penup()
        goto(poziceX+(ctverec/2), poziceY-ctverec+4)
        pendown()
        circle((ctverec/2)-4)
    hrac = not hrac

print("Konec hry")
exitonclick()