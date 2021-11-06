from turtle import circle, forward, left, right, exitonclick, speed, penup, pendown, goto, color, pensize 

strana_ctverce = 50                                       
while(True):                                                
    radek = (input('Zadej počet řádků:'))
    
    # ošetření proti zadání písmena                
    if not radek.isnumeric():                               
        print("Zkus to znovu a zadej celé kladné číslo")    
        continue                                          

    radek = int(radek)                                      
    
    # ošetření proti zadání nuly
    if(radek == 0):                                         
        print("Zkus to znovu a zadej celé kladné číslo")  
    else:
        break                                            

while(True):                                                
    sloupec = (input('Zadej počet sloupců:'))
    
    # ošetření proti zadání písmena 
    if not sloupec.isnumeric():
        print("Zkus to znovu a zadej celé kladné číslo")
        continue

    sloupec = int(sloupec)
    
    # ošetření proti zadání nuly
    if(sloupec == 0):
        print("Zkus to znovu a zadej celé kladné číslo")
    else:
        break

# vykreslení hracího pole
speed(0)
pensize (3)
for _ in range(radek):                                     
    for _ in range(sloupec):                            
        for _ in range(4):
            forward(strana_ctverce)
            left(90)
        forward(strana_ctverce)
    left(180)
    forward(sloupec*strana_ctverce)
    right(90)
    forward(strana_ctverce)
    right(90)

print("Souřadnice jsou číselné pro osu x a pro osu y zvlášt, levé horní pole je označeno jako 1X 1Y, pravé dolní pole jako nX a nY")

hrac = True                                                                                           

# hlavní herní smyčka
for _ in range(sloupec*radek):                             
    
    # vypisujeme který hráč je na tahu
    if(hrac):                                              
        print("Hraje hráč X")
    else:
        print("Hraje hráč O")
    
    # výběr souřadnice x
    while(True):                                                                           
        x = input("Zadej souřadnici x: ")                  
        if not x.isnumeric():                              
            print("Zkus to znovu a zadej správnou souřadnici")
            continue

        x = int(x)

        # ošetření proti zadání čísel, které nejsou souřadnicemi
        if(x <= 0 or x > sloupec):                         
            print("Zkus to znovu a zadej správnou souřadnici")
        else:
            break
    
    # výběr souřadnice y
    while(True):                                           
        y = input("Zadej souřadnici y: ")
        if not y.isnumeric():
            print("Zkus to znovu a zadej správnou souřadnici")
            continue

        y = int(y)

        # ošetření proti zadání čísel, které nejsou souřadnicemi
        if(y <= 0 or y > radek):
            print("Zkus to znovu a zadej správnou souřadnici")
        else:
            break
    

    # zapsány jsou také dvě proměnné pro posun pera z nulových souřadnic na souřadnice vybraného pole
    poziceX = (x-1)*strana_ctverce                       
    poziceY = (radek+1-y)*strana_ctverce                
    
    # vykreslení pole hráče X
    if hrac:                                              
        color('blue')                                    
        penup()
        goto(poziceX, poziceY)                         
        pendown()
        goto(poziceX+strana_ctverce, poziceY-strana_ctverce)            
        penup()
        goto(poziceX+strana_ctverce, poziceY)
        pendown()
        goto(poziceX, poziceY-strana_ctverce)
    
    # vykreslení pole hráče O
    else:                                             
        color('red')
        penup()
        goto(poziceX+(strana_ctverce/2), poziceY-strana_ctverce+4)
        pendown()
        circle((strana_ctverce/2)-4)
    
    # změna hráče
    hrac = not hrac                                       

print("Konec hry")                                    
exitonclick()