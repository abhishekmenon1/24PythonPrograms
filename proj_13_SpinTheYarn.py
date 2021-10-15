"""
The program first prompts the user to enter a series of inputs. These can be an adjective, a preposition, a proper noun, etc.
Once all the inputs are in place, they are placed in a premade story template using concatenation.
"""

title = '\nWelcome to Spin the Yarn. Answer the following Questions and read the story!\n'
print(title)

char_name = input("Give me 2 names of people(i.e Ross, Racheal): ")
char_list = char_name.split(",")

action = input("Tell me a vehicle you'd like to drive(i.e motorbike, Merecedes): ")
action_list = action.split(",")

places =input("Give me 2 places you'd like to visit(i.e Rome, Milan): ")
places_list = places.split(",")

age = input("Finally, How old are you? ")

sen1 = "A Long time ago, let's say "+ age + " years ago," + char_list[1] + " was looking to buy a LED TV."
sen2 = "Another person named "+char_list[0]+" was actually interested in selling their TV."
sen3 = "\nThe only problem was "+char_list[0]+" lived in "+places_list[0]+" and "+char_list[1]+" lived in "+places_list[1]+"."
sen4 = "Therefore, " + char_list[0] + " decided to jump into the "+action_list[0]+" in the garage and raced over to"+ places_list[1]+ "."

print(sen1, sen2, sen3, sen4)