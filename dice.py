#/usr/bin/python3
import random
import os,sys

class Dice(object):

    """Dice class handles dices configuration and rolling of the dice."""

    def __init__(self, num_sides, dice_id):
        """ * num_sides     number of sides for a dice 
            * dice_id       id of the created dice
        """
        self.num_sides = 6
        self.id = dice_id

    def roll(self):
        roll = random.randint(1,self.num_sides)
        print(f'Dice [{self.id}] roll is: {roll}')

class Hand(object):

    """Hand class handles rolling of all dices in the hand. It takes care of 
       dice_ids and number of sides 
    """

    def __init__(self, num_dices, num_sides):
        self.dices = [ Dice(num_sides, dice_id) for dice_id in range(1,num_dices+1) ]

    def roll(self):
        for dice in self.dices:
            dice.roll()

    def update(self, num_dices, num_sides):
        #Sanity check:
        if num_dices>0 and num_dices<5:
            self.num_dices = num_dices
            print(f"Number of dices set to {num_dices}")
        else:
            print("Wrong number of dices, configuration failed")

        if num_sides >= 4 and num_sides <=20:
            self.num_sides = num_sides
            print(f"Number of sides set to {num_sides}")
        else:
            print("Wrong number of sides, configuration failed")
        self.dices = [ Dice(self.num_sides, dice_id) for dice_id in range(1,self.num_dices+1) ]

    def update_from_string(self, string):
        num_dices_str, num_sides_str = string.split("d")
        num_dices = int(num_dices_str)
        num_sides = int(num_sides_str)
        if num_dices >= 1 and num_dices < 5 and num_sides >= 4 and num_sides <= 20:
            self.num_dices = num_dices
            self.num_sides = num_sides
            self.update(self.num_dices, self.num_sides)
        else:
            print("!! Wrong number of dices or sides !!")



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
    hand = Hand(num_dices, num_sides)

    line = None
    print("Type help for commands, exit to exit")
    while True: 
        line = input(f"Roll {num_dices}d{num_sides}? >> ")

        if line == "exit":
            exit(0)

        elif line == "":
            hand.roll()

        elif int(line[0]) in range(1,10):
            hand.update_from_string(line)
            hand.roll()

        elif line == "config":
            print("=> Configure dices and sides ")
            num_dices_in = int(input("   - Number of dices: "))
            num_sides_in = int(input("   - Number of sides: "))


        elif line == "help":
            print("Press ENTER for a roll, or type a command for other options")
            print("Available commands: ")
            print("help      prints this help message")
            print("config    starts the configuration wizard")
            print("exit      exits the program")

        else:
            print("!! Command not understood. See help for more info !!")


if __name__ == "__main__":
    main()

