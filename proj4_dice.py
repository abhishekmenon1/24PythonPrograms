'''
Generate a random number each dice the program runs,
 and the users can use the dice repeatedly for as long as he wants. When the user rolls the dice, the program
  will generate a random number between 1 and 6 (as on a standard dice).
The number will then be displayed to the user. It will also ask users if they would like to roll the dice again.
The program should also include a function that can randomly grab a number within 1 to 6 and print it.
'''

import random

def dice():
    number = random.randint(1,6)
    print('The dice rolled', number,"!")

for i in range(0,1000):
    ask= input("\nDo you want to roll the dice? Enter Yes: ")
    if ask == 'Yes' or ask =='yes':
        dice()
    else:
        break
