import random

def dice(dice1):# defines the word dice
    number = random.randint(1,6)#code for dice(RANOM NUMBER GENORATOR)
    print(number)#prints the result of the dice
    
def cards():
    card1 = input("search card here ::")
    if card1 == ("panther"):
        f = open("[file structure here]") #like this 'cards/tanks/panther.txt'
                                          #it depends on what file but is you do 'windows key + e' you can open file explorer and find the file path and copy it there should be a button if there isnt get good
        print(f.read())  
    
        

while True:
    print("                                 6 sided dice = 1 ")#gives option
    print("                                 combat cards = 2") #gap for looks
    dice1 = input("                         select an option") #this looks shit get rid of it 
    if dice1 == ("1"):
        dice(dice1)
    elif dice1 == ("2"):
     cards()
