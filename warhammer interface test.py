import random

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
        print('What would you like to accsess')
        print('1) Troops')
        print('2) Tanks')
        print('3) Planes')
        print('4) Misc')
        inp = input()
        if inp == '1':
            print('one')
        elif inp == '2':
            print('two')
        elif inp == '3':
            print('three')
        elif inp == '4':
            print('four')

def rules():
    print('What rule book would you like to access')
    print('1) Our bolt-action')
    print('2) Bolt-action')
    inp = input()
    if inp == '1':
        rules = open('modified-bolt-action-rules.txt')

while True:
    print('Welcome to the Bolt Action TUI')
    print('What would you like to do')
    print('1) Dice roller')
    print('2) Cards')
    print('3) Rule book')
    prog = input('Enter the number corisponding to the thing you would like to accsess or "home" to exit: ')
    if prog == '1':
        dice_roller()
    elif prog == '2':
        cards()
    elif prog == '3':
        rules()
