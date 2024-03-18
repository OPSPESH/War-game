import random

def dice(dice1):# defines the word dice
    number = random.randint(1,6)#code for dice(RANOM NUMBER GENORATOR)
    print(number)#prints the result of the dice

while True:
    print("6 sided dice = 1 ")#gives option
    print("combat cards = 2") #gap for looks
    dice1 = input("select an option   ")
    if dice1 == ("1"):
        dice(dice1)
    elif dice1 == ("2"):
         dice1 = input("search card here ::")
    if dice1 == ("infantry"):
        f = open("H:/card game/card basic all infantry.txt")
        print(f.read())
       
  
 
