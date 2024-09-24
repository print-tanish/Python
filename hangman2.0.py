import random

def choose_word():
    words = ['papaya','apple']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. {attempts} attempts left.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word '{word}' correctly.")
            break
    else:
        print(f"\nGame Over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
