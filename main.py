import random

import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hangman")
print(ascii_banner)

word_list = ["aardvark", "baboon", "camel"]
players_choice = input("What a letter: ".lower())

random_word = random.choice(word_list)

for letter in random_word:
    if letter == players_choice:
        print("Yes")

    else:
        print("No")

