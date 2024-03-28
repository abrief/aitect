import random

def guess_number_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guess = None
    number_of_guesses = 0

    print("Guess the number! It's between 1 and 100.")

    # Loop until the user guesses the number
    while guess != number_to_guess:
        # Get the user's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        number_of_guesses += 1

        # Check the guess
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number in {number_of_guesses} tries.")
            break

if __name__ == "__main__":
    guess_number_game()
