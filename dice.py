'''
source: https://www.dieharddice.com/pages/dnd-dice-explained
To start playing, you only need one of each: the D4, D6, D8, D10, D12, and D20,
but standard 7-dice sets also include a second D10 which is used for percentile rolls.
Gamers often prefer to have multiples of some die in order to roll pools of dice, such as 3D6 in one roll instead of 3 individual d6 rolls.

As a nerd I would like to present a DnD dice simulator

'''

import random

dice = int(input("Which dice would you like to use? "))
print(f'Sure, D{dice} it is!')

toss = 0
if dice == 4:
    toss = random.randint(1,4)
elif dice == 6:
    toss =random.randint(1,6)
elif dice == 8:
    toss = random.randint(1,8)
elif dice == 10:
    toss = random.randint(1,10)
elif dice == 12:
    toss = random.randint(1,12)
elif dice == 20:
    toss = random.randint(1,20)
else: print("Once again please")


print(f'I wish you luck... You rolled {toss}')
