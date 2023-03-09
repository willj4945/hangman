import random

import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hangman")
print(ascii_banner)

word_list = ["aardvark", "baboon", "camel"]

chosen_word = ""
players_choice = input("What is the random word? ".lower())

for i in range(1):
    chosen_word = random.choice(word_list)
    print(chosen_word)

if players_choice == chosen_word:
    print("Player wins!")
else:
    print("Player losses")
