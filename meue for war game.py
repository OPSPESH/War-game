import random
def dice(dice1):# defines the word dice
    number = random.randint(1,6)#code for dice(RANOM NUMBER GENORATOR)
    print(number)#prints the result of the dice
    if dice1 == 'home':
        return
    
def cards():
    card1 = input("search card here ::")
    if card1 == ("panther"):
        f = open("card basic all infantry*,txt", "r")
        print(f.read())  
    
        

while True:
    print("                                 6 sided dice = 1 ")#gives option
    print("                                 combat cards = 2") #gap for looks
    dice1 = input("                         select an option")
    if dice1 == ("1"):
        dice(dice1)
    elif dice1 == ("2"):
     cards()
  
 
