# Jared West
# CS500 In the spotlight "dice roll"
# Mr. Chou

# This program simulates the rolling of a 20-sided dice
import random

# Global CONSTANTS for min and max values
MIN = 1
MAX = 20

def main():
    again = 'y'  # Create a variable to control the loop
    print('Welcome to the D20 roller, for all of your DnD needs!')
    print(f'We are simulating rolling of a {MAX}-sided dice.')

    # Simulate the rolling of dice
    while again.lower() in ['y', 'yes']:
        print("Rolling the dice. . . ")
        print("Their values are: ")
        print(f"Your dice roll is: {random.randint(MIN, MAX)}")
        print(f"Your dice roll is: {random.randint(MIN, MAX)}")
        print(f"Your dice roll is: {random.randint(MIN, MAX)}")

        # Do you want to roll again?
        again = input("Do you want to roll again? Y = yes: ")

main()  # Call for main function
