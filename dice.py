#/usr/bin/python3
import random
import os,sys

def main():
    if len(sys.argv) < 2:
        print("Wrong number of arguments!")
        return 1
    else:
        num_dices = int(sys.argv[1])
        for dice in range(num_dices):
            roll = random.randint(1,6)
            print(f'Dice [{dice+1}] roll is: {roll}')


if __name__ == "__main__":
    main()

