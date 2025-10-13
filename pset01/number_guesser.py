# ----------------------------------------------------------------------
# This is the file number_guesser.py
#
# The intent is to give you practice writing a complete, interactive
# Python program.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#
# Generate a random number between 1 and 1000.
#
# Ask the user to guess the number. In your prompt, let the user know they
# can type 'bye' or 'exit' to quit the program.
#
# If their guess is not made up entirely of digits, print "Please enter a valid
# number" and ask them to guess again.
#
# If the guess is too high, print "Too high!" and continue asking.
#
# If the guess is too low, print "Too low!" and continue asking.
#
# If the guess is correct, print "Congratulations! You guessed the number!" along
# with the number of attempts it took to guess the number. Start over with a new
# random number. Make sure to zero out the number of attempts.
#
# Please note: There are likely to be a number of Python guessing games online,
# and most GenAI systems can probably write this for you. Don’t rely on them,
# as they rob you of a chance to practice your Python skills and they might not
# even be correct. Perhaps, worse, they might not follow the instructions
# exactly as given.
# ----------------------------------------------------------------------

import random

def number_guesser():
    number_to_guess = random.randint(1, 1000)
    attempts = 0

    while True:
        user_input = input("Guess a number between 1 and 1000 (or type 'bye' or 'exit' to quit): ")

        if user_input.lower() in ['bye', 'exit']:
            print("Thanks for playing! Goodbye!")
            break

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!")
            number_to_guess = random.randint(1, 1000)
            attempts = 0

if __name__ == "__main__":
    number_guesser()
