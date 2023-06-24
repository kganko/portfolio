# Hangman Game

import random
wordlist = ["Grease", "Dirty Dancing", "Mamma Mia", "Phantom of the Opera"]


word = random.choice(wordlist)
final = list(word)
mystery = str(len(word)*"_")
print(f'Hello Dear Gamer! Are you ready for a challenge? This is your word: {mystery}')

mysterylist = []

for everyletter in final:
    mysterylist.append(everyletter)

print(mysterylist)

# Stores the correct letters in the word
correct = []
incorrect = []

currentstate = []
separateletter= 0
currentstate = mysterylist

chancesleft = 6

def check_win(currentstate):
    for char in currentstate:
        if letter == '_':
            return False
    return True

for i in range(chancesleft+1):
    letter = input("Please guess your letter: ")

    if letter not in mysterylist:
        chancesleft = chancesleft - 1
        print(f'You lose one chance! Amount of chances left {chancesleft}')
    else:

        for i in range(len(mystery)):
            if mysterylist[i] == letter:
                currentstate[i] = letter
            else: currentstate[i] = "_"
        print(currentstate)
        print(mysterylist)
        print(f"you still have {chancesleft} chances")

next
