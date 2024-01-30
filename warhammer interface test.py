import random, os 

def dice_roller():
    while True:
        num = input('Enter a number from [1-20] or "home" to exit')
        if num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']:
            res_list = [random.randint(1,6) for i in range(int(num))]
        elif num == 'home':
            return 
        print(res_list)

def cards():
    while True:
        print('What would you like to accsess or "home" to close: ')
        print('1) Troops')
        print('2) Tanks')
        print('3) Planes')
        print('4) Misc')
        inp = input()
        if inp == '1':
            print('one')
        elif inp == '2':
            print(os.listdir('cards/tanks'))
            inp = input('Select a card')
            if inp == 'churchhill':
                card = open('cards/tanks/churchhill.txt')
                print('')
                print(card.read())
                print('')
                card.close()
            elif inp == 'stug3' or 'stug-3':
                card = open('cards/tanks/stug-3.txt')
                print('')
                print(card.read())
                print('')
                card.close()
        elif inp == '3':
            print(os.listdir('cards/planes'))
            inp = input('Select a card')
            if inp == 'spitfire':
                card = open('cards/planes/spitfire.txt')
                print('')
                print(card.read())
                print('')
                card.close()
            elif inp == 'typhoon' or 'hawker typhoon':
                card = open('cards/planes/hawker typhoon.txt')
                print('')
                print(card.read())
                print('')
                card.close()
            if inp == 'messerschmitt':
                card = open('cards/planes/messerschmitt.txt')
                print('')
                print(card.read())
                print('')
                card.close()
        elif inp == '4':
            print('four')
        elif inp == 'home':
            return

def rules():
    while True:
        print('What rule book would you like to access: ')
        print('1) semi-action')
        inp = input()
        if inp == '1':
            file = open('semi-action-rules.txt')
            print(file.read())
            print('')
            
while True:
    print('Welcome to the Bolt Action TUI')
    print('What would you like to do')
    print('1) Dice roller')
    print('2) Cards')
    print('3) Rule book')
    prog = input('What would you like to accsess or "home" to exit: ')
    if prog == '1':
        dice_roller()
    elif prog == '2':
        cards()
    elif prog == '3':
        rules()
    elif prog == 'home':
        exit()
