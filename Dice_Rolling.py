import random

def roll(sides):
    return random.randint(1, sides)

def main():
    sides = 6
    rolling = True
    while rolling:
        ask_roll = input("Ready to roll? ENTER=Roll or Q=Quit ")
        if ask_roll.lower() != "q":
            print("You rolled a " + str(roll(sides)))
        else:
            rolling = False

if __name__ == "__main__":
    main()