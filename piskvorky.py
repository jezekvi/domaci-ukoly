from turtle import forward, left, right, exitonclick, speed

while(True):
    x = (input('Zadej délku strany čtverce:'))
    if not x.isnumeric():
        print("Zkus to znovu a zadej celé kladné číslo")
        continue
    x = int(x)
    if(x == 0):
        print("Zkus to znovu a zadej célé kladné číslo")
    else:
        break
speed(0)
for _ in range(3):
    for _ in range(3):
        for _ in range(4):
            forward(x)
            left(90)
        forward(x)
    left(180)
    forward(3*x)
    right(90)
    forward(x)
    right(90)

exitonclick()