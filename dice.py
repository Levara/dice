#/usr/bin/python3
import random
import os,sys

def parse_params():
    if len(sys.argv) == 2:
        num_dices = int(sys.argv[1])
        num_sides = 6
    elif len(sys.argv) == 3:
        num_dices = int(sys.argv[1])
        num_sides = int(sys.argv[2])
    else:
        print("Wrong number of arguments!")
        print("Usage: python dice.py [number_of_dices] [number_of_sides]")
        exit(1)
    return [num_dices, num_sides]

def main():
    num_dices, num_sides = parse_params()

    line = None
    print("Type help for commands, exit to exit")
    while True: 
        line = input("Roll? >> ")

        if line == "exit":
            exit(0)
        elif line == "config":
            print("=> Configure dices and sides ")
            num_dices_in = int(input("   - Number of dices: "))
            num_sides_in = int(input("   - Number of sides: "))

            #Sanity check:
            if num_dices_in>0 and num_dices_in<5:
                num_dices = num_dices_in
                print(f"Number of dices set to {num_dices}")
            else:
                print("Wrong number of dices, configuration failed")

            if num_sides_in >= 4 and num_sides_in <=20:
                num_sides = num_sides_in
                print(f"Number of sides set to {num_sides}")
            else:
                print("Wrong number of sides, configuration failed")

        elif line == "help":
            print("Press ENTER for a roll, or type a command for other options")
            print("Available commands: ")
            print("help      prints this help message")
            print("config    starts the configuration wizard")
            print("exit      exits the program")

        elif line == "":
            for dice in range(num_dices):
                roll = random.randint(1,num_sides)
                print(f'Dice [{dice+1}] roll is: {roll}')

if __name__ == "__main__":
    main()

