#/usr/bin/python3
import random
import os,sys

def main():
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print("Wrong number of arguments!")
        return 1
    elif len(sys.argv) == 2:
        num_dices = int(sys.argv[1])
        num_sides = 6
    elif len(sys.argv) == 3:
        num_dices = int(sys.argv[1])
        num_sides = int(sys.argv[2])

    for dice in range(num_dices):
        roll = random.randint(1,num_sides)
        print(f'Dice [{dice+1}] roll is: {roll}')


if __name__ == "__main__":
    main()

