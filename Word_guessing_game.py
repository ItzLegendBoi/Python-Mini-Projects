"""Word Guessing Game (Hangman style)."""
import random

WORDS = ["python", "variable", "function", "program", "keyboard", "internet",
         "algorithm", "developer", "compiler", "database"]

def play():
    word = random.choice(WORDS)
    guessed, lives = set(), 6
    while lives > 0:
        shown = " ".join(c if c in guessed else "_" for c in word)
        print(f"\nWord: {shown}   Lives: {lives}   Guessed: {' '.join(sorted(guessed))}")
        if "_" not in shown:
            print("You won!")
            return
        letter = input("Guess a letter: ").lower().strip()
        if len(letter) != 1 or not letter.isalpha():
            print("Enter a single letter.")
        elif letter in guessed:
            print("Already guessed.")
        else:
            guessed.add(letter)
            if letter not in word:
                lives -= 1
                print("Wrong!")
    print(f"Game over. The word was '{word}'.")

if __name__ == "__main__":
    while True:
        play()
        if input("\nPlay again? (y/n): ").lower() != "y":
            break
