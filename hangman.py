import urllib.request
import random
from PyDictionary import PyDictionary
import os

# Download the SOWPODS word list if not already downloaded
#if file is not found, then download it
if not os.path.exists('sowpods.txt'):
    url = 'https://raw.githubusercontent.com/jesstess/Scrabble/refs/heads/master/scrabble/sowpods.txt'
    urllib.request.urlretrieve(url, 'sowpods.txt')

dictionary = PyDictionary()

def pick_word():
    with open('sowpods.txt') as f:
        words = f.readlines()
    return random.choice(words).strip()

def display_word(word, guessed):
    return ' '.join(c if c in guessed else '_' for c in word)

def game():
    word = pick_word().upper()
    guessed = set()
    attempts = 6

    while attempts > 0:
        print(display_word(word, guessed))
        letter = input('Enter a letter (or type "I GIVE UP" to reveal the word): ').strip().upper()

        if letter == "I GIVE UP":
            print(f"The word was: {word}")
            definition = dictionary.meaning(word)
            if definition:
                for key, value in definition.items():
                    print(f"{key}: {', '.join(value)}")
            else:
                print("Definition not found.")
            break

        if letter in guessed:
            print('You already guessed that letter')
            continue

        guessed.add(letter)

        if letter in word:
            if all(c in guessed for c in word):
                print('You won!')
                print(word)
                definition = dictionary.meaning(word)
                if definition:
                    for key, value in definition.items():
                        print(f"{key}: {', '.join(value)}")
                else:
                    print("Definition not found.")
                break
        else:
            print('The letter is not in the word')
            attempts -= 1
            print(f"Attempts remaining: {attempts}")

        if attempts == 0:
            print(f"You lost! The word was: {word}")
            definition = dictionary.meaning(word)
            if definition:
                for key, value in definition.items():
                    print(f"{key}: {', '.join(value)}")
            else:
                print("Definition not found.")

while True:
    game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        break
