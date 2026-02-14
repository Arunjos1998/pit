import random

def word_scramble_game():
    # List of words to choose from
    words = ['python', 'programming', 'computer', 'game', 'developer', 'artificial', 'intelligence', 'machine', 'learning']
    
    # Randomly choose a word from the list
    word = random.choice(words)
    
    # Scramble the word
    scrambled_word = ''.join(random.sample(word, len(word)))
    
    print("Welcome to the Word Scramble Game!")
    print(f"Scrambled word: {scrambled_word}")
    
    # Player has 3 attempts to guess the word
    attempts = 3
    
    while attempts > 0:
        guess = input(f"You have {attempts} attempts left. Unscramble the word: ").lower()
        
        if guess == word:
            print("Congratulations! You guessed the word correctly!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print("Oops! Try again!")
            else:
                print(f"Sorry, you've run out of attempts. The word was: {word}")

# Start the game
word_scramble_game()
