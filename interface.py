import random, os, sys

def dice_roller():
    while True:
        num = input("[1-20] or 'close' to exit")
        if num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']:
            res_list = [random.randint(1,6) for i in range(int(num))]
        elif num == 'close':
            return 
        print(res_list)

def cards():
        while True:
            print('1) Troops')
            print('2) Tanks')
            print('3) Planes')
            print('4) Misc')
            inp = input("'close' to exit")
            if inp == '1':
                print(os.listdir('cards/troops'))
                inp = input('Select a card')
                if inp == 'anti tank':
                    card = open('cards/troops/anti_tank.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
                elif inp == 'heavy machine gun' or inp == 'hmg':
                    card = open('cards/troops/heavy_machine_gun.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
                elif inp == 'lmg':
                    card = open('cards/troops/lmg.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
                elif inp == 'rifle':
                    card = open('cards/troops/rifle.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
                elif inp == 'sniper':
                    card = open('cards/troops/sniper.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
            elif inp == '2':
                print(os.listdir('cards/tanks'))
                inp = input('Select a card')
                if inp == 'churchhill':
                    card = open('cards/tanks/churchhill.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
                elif inp == 'sherman':
                    card = open('cards/tanks/sherman.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
                elif inp == 'stug3' or inp == 'stug-3':
                    card = open('cards/tanks/stug-3.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
            elif inp == '3':
                print(os.listdir('cards/planes'))
                inp = input('Select a card')
                if inp == 'hawker typhoon':
                    card = open('cards/planes/hawker_typhoon.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
                elif inp == 'messerchmitt':
                    card = open('cards/planes/messerchmitt.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
                elif inp == 'spitfire':
                    card = open('cards/planes/spitfire.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
            elif inp == '4':
                print(os.listdir('cards/misc'))
                inp = input('Select a card')
                if inp == '5.5 inch gun':
                    card = open('cards/misc/5.5-inch_gun.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
                elif inp == '6pdr anti tank gun':
                    card = open('cards/misc/6pdr_anti_tank_gun.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
                elif inp == 'aec matador':
                    card = open('cards/misc/aec_matador.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
                elif inp == 'bofors_gun':
                    card = open('cards/misc/bofors_gun.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
                elif inp == 'bren gun carrier':
                    card = open('cards/misc/bren_gun_carrier.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
                elif inp == 'morris cs8':
                    card = open('cards/misc/morris_cs8.txt')
                    print('')
                    print(card.read())
                    print('')
                    card.close()
            elif inp == 'close':
                return

def rules():
    while True:
        print('1) semi-action')
        inp = input("'close' to exit")
        if inp == 'close':
            return
        elif inp == '1':
            file = open('semi-action-rules.txt')
            print(file.read())
            print('')
            file.close()
while True:
    print('1) Dice roller')
    print('2) Cards')
    print('3) Rule book')
    prog = input("'close' to exit: ")
    if prog == '1':
        dice_roller()
    elif prog == '2':
        cards()
    elif prog == '3':
        rules()
    elif prog == 'close':
        sys.exit(0)
