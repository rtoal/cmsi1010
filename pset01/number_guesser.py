import random

number_to_guess = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100 (or type 'bye' or 'exit' to quit): ")

    # Check for exit conditions and legal input
    if guess.lower() in ['bye', 'exit']:
        print("Thanks for playing! Goodbye!")
        break
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    # Ok, if you got here, you know its a valid guess, so you can count
    # the attempt and check the guess
    attempts += 1
    if int(guess) < number_to_guess:
        print("Too low! Try again.")
    elif int(guess) > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} tries!")

        # Get new number and reset attempt count for the next game
        number_to_guess = random.randint(1, 100)
        attempts = 0

