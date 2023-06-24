'''
madlib stolen from: https://madlibs.bostonchildrensmuseum.org/madlibs/spy.php
'''

from tkinter import *

# a lot of inputs from the user
print ("Yay! Let's play madlib game! Don't ruin this and follow input instructions:")
blank1 = input("plural noun: ")
blank2 = input("adjective: ")
blank3 = input("person in room(male): ")
blank4 = input("number: ")
blank5 = input("adjective: ")
blank6 = input("noun: ")
blank7 = input("part of the body: ")
blank8 = input("adjective: ")
blank9 = input("part of the body: ")
blank10 = input("adjective: ")
blank11 = input("plural noun: ")
blank12 = input("noun: ")
blank13 = input("part of the body: ")
blank14 = input("noun: ")
blank15 = input("noun: ")
blank16 = input("verb: ")
blank17 = input("celebrity: ")
blank18 = input("noun: ")

# check intelligence of the user
if not all([blank1, blank2, blank3, blank4,blank5, blank6, blank7, blank8,blank9, blank10, blank11, blank12, blank13, blank14, blank15, blank16, blank17, blank18]):
   print ("Oh come on, don't ruin the game!")
   exit()

text = (f'The Spy Hall of Fame honors the brave {blank1} of that {blank2} profession known as spying. Inductees include'
        f'{blank3}Bond—Famously known as Agent Double "O" {blank4}, this spy was as handsome as he was {blank5}. Not only did Bond nab the bad {blank6} every time, he always won the {blank7} of the {blank8} woman as well.'
        f'Chuck Eagle {blank9} Spyglass—Whether it was designing a/an {blank10} pair of night-vision {blank11} or hiding a tiny camera inside a gold {blank12} that a spy could wear around his {blank13}, Chuck was the go-to {blank14} for his wizardry in surveillance.'
        f'Joe the Spy—Joe was your typical {blank15} next door. His high school yearbook denoted him as "Most Likely to {blank16}." Who would have thought this Average Joe would be the {blank17} of the spy world when he single-handedly took down an international ring of {blank18} robbers?!')

#display
win=Tk()
txt= Text(win, height=45, width=180)
txt.pack()
txt.insert(INSERT,"let's play madlib!")
txt.insert(END, text)
win.mainloop()