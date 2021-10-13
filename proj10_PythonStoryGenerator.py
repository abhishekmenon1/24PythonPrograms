"""
This is a fun but exciting python project which will work wonders with kids.
In a nutshell, the program will ask users for inputs such as the name of a place, action, etc.
 and then build a story around the data.
The story will be the same always but with little variation with the input.
"""

import random
def story(name, food, friend, action):
    i = random.randint(1,3)
    if i == 1:
        print("\n-----\nThere was once a young boy named",name,"who loved to eat candy.")
        print("After eating all the candy",name,"was still hungry. So he decided to the market to buy some delicious",food)
        print("There was only ONE serving left of the",food,"so he ran to grab it but his arch nemesis",friend,"grabbed it before he could.")
        print("In anger",name,"decided to", action.upper(),"!")

    if i == 2:
        print("\n-----\nLong ago in a barron land, King",name,"ruled a nation of many")
        print("Despite being the greatest leader known to mankind, King",name,"had one weakness....",food.upper(),"!")
        print("The only problem was that",food,"was also his pet monkey's favourite food. The monkey's name was,",friend,".")
        print("Therefore, to distract",friend,", King",name,"would",action,"very passionately and slyly snatch the",food,"away.")

    if i == 3:
        print("\n----\nyou should actually go to sleep.")

title = "Welcome to Story Generator!"
print(title)

name = input("Enter a name: ")
food = input("Enter a name of your favourite food: ")
friend = input("Enter you best friend's name: ")
action = input("Complete this sentence with ONE verb. I like to ___ ")

story(name, food, friend, action)

