'''
Proyecto Hangman en Python by fjga
Comentario adicional para probar Git Hub
otro cambio más........

Otro nuevo cambio
'''

import random
from string import ascii_lowercase

word_list = ['python', 'java', 'kotlin', 'javascript']

# Welcome message
print("H A N G M A N")
while True:
    game = input('Type "play" to play the game, "exit" to quit:')
    if game == 'play':
        word_selec = random.choice(word_list)
        char_word_selec = set(word_selec)
        char_word_rest = set(word_selec)
        char_input = set()
        char_ok = set()
        count = 0
        while count < 8:
            word_guess = word_selec
            for letter in char_word_rest:
                word_guess = word_guess.replace(letter, "-")
            print()
            print(word_guess)
            char = input('Input a letter: ')
            if len(char) != 1:
                print('You should print a single letter')
            elif char not in ascii_lowercase:
                print('It is not an ASCII lowercase letter')
            elif char in char_input or char in char_ok:
                print('You already typed this letter')
            elif char in word_selec:
                char_ok.add(char)
                char_word_rest.remove(char)
                if char_ok == char_word_selec:
                    print(f"You guessed the word {word_selec}!")
                    print("You survived!")
                    break
            else:
                print('No such letter in the word')
                count += 1
                char_input.add(char)
        else:
            print("You are hanged!")
    elif game == 'exit':
        break
