import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Type 'q' anytime to quit.\n")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ")

        if guess.lower() == 'q':
            print(f"The number was {number}. Thanks for playing!")
            break

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts!")
            break
        elif abs(guess - number) <= 5:
            print("🔥 Very close!")
        elif guess < number:
            print("📉 Too low!")
        else:
            print("📈 Too high!")

if __name__ == "__main__":
    number_guessing_game()
