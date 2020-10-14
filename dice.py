#/usr/bin/python3
import random
import os,sys

def main():
    if len(sys.argv) == 2:
        num_dices = int(sys.argv[1])
        num_sides = 6
    elif len(sys.argv) == 3:
        num_dices = int(sys.argv[1])
        num_sides = int(sys.argv[2])
    else:
        print("Wrong number of arguments!")
        print("Usage: python dice.py [number_of_dices] [number_of_sides]")
        return 1

    for dice in range(num_dices):
        roll = random.randint(1,num_sides)
        print(f'Dice [{dice+1}] roll is: {roll}')


if __name__ == "__main__":
    main()

