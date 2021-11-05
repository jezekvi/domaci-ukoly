from turtle import circle, forward, left, right, exitonclick, speed, penup, pendown, goto, color, pensize  # import potřebných příkazů

ctverec = 50                                                # konstanta délky strany čtverce
while(True):                                                # pracujeme s True kvůli isnumeric, 
    radek = (input('Zadej počet řádků:'))                   # nejdříve zadáváme počet řádků
    if not radek.isnumeric():                               # ošetření proti zadání písmena je vytvořeno pomocí isnumeric, který vrací True, pokud jsou zadané číselné znaky.  
        print("Zkus to znovu a zadej celé kladné číslo")    
        continue                                            # cyklus se opakuje dokud uživatel nezadá správnou hodnotu

    radek = int(radek)                                      # přepis proměnné na intiger (do isnumeric můžeme totiž zapsat i jiné hodnoty než celá čísla a to my nechceme)
    if(radek == 0):                                         # ošetření proti zadání nuly
        print("Zkus to znovu a zadej célé kladné číslo")  
    else:
        break                                               # ukončení cyklu

while(True):                                                # stejný postup je použit i u sloupců
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
for _ in range(radek):                                     # na následujících řádcích je zapsán princip vykreslení hracího pole
    for _ in range(sloupec):                               # pracujeme s konstantami radek a sloupec, kvůli různým velikostem pole podle zadání uživatele
        for _ in range(4):
            forward(ctverec)
            left(90)
        forward(ctverec)
    left(180)
    forward(sloupec*ctverec)
    right(90)
    forward(ctverec)
    right(90)


hrac = True                                                # zadání proměnné hráč (střídání hráčů funguje na principů střídání hodnot True a False - zasadní je pro to řádek 93)                                            

for _ in range(sloupec*radek):                             # zde je zapsán počet tahů ve for cyklu, tedy celkový počet polí
    if(hrac):                                              # vypisujeme který hráč je na tahu (následuje výběř souřadnic)
        print("Hraje hráč X")
    else:
        print("Hraje hráč O")
    while(True):                                           # princip zápisu souřadnic je stejný jako u hracího pole (první hraje hráč X, protože je hodnocen jako True)                                 
        x = input("Zadej souřadnici x: ")                  # souřadnice jsou číselné pro osu x a pro osu y zvlášt, levé horní pole je označeno jako 1X 1Y, pravé dolní pole jako nX a nY
        if not x.isnumeric():                              # opět pracujeme s isnumeric
            print("Zkus to znovu a zadej správnou souřadnici")
            continue

        x = int(x)
        if(x <= 0 or x > sloupec):                         # ošetření proti zadání čísel, které nejsou souřadnicemi. Tedy menší a stejné 0 a větší než počet sloupců
            print("Zkus to znovu a zadej správnou souřadnici")
        else:
            break

    while(True):                                           # stejný postup pro y
        y = input("Zadej souřadnici y: ")
        if not y.isnumeric():
            print("Zkus to znovu a zadej správnou souřadnici")
            continue

        y = int(y)
        if(y <= 0 or y > radek):
            print("Zkus to znovu a zadej správnou souřadnici")
        else:
            break
    
    poziceX = (x-1)*ctverec                                # zapsány jsou také dvě proměnné pro posun pera z nulových zouřadnic na souřadnice vybraného pole
    poziceY = (radek+1-y)*ctverec                
    
    if hrac:                                               # vykreslujeme pole hráče x (stále jsme pod prvním for cyklem)
        color('blue')                                      # v tomto případě zakreslujeme křížek
        penup()
        goto(poziceX, poziceY)                         
        pendown()
        goto(poziceX+ctverec, poziceY-ctverec)            
        penup()
        goto(poziceX+ctverec, poziceY)
        pendown()
        goto(poziceX, poziceY-ctverec)
    else:                                                 # přes else se dostaneme i k druhému hráči, který zakresluje kruh
        color('red')
        penup()
        goto(poziceX+(ctverec/2), poziceY-ctverec+4)
        pendown()
        circle((ctverec/2)-4)
    hrac = not hrac                                       # tento řádek je zásadní pro výměnu hráčů (otočíme totiž hodnoty true a false pro proměnnou hrac)                                 

print("Konec hry")                                        # po ukončení cyklu (počet tahů podle počtu polí vypíšeme konec hry)
exitonclick()