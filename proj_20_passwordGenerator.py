# Creating a strong password and remembering it is a tedious task. You can build a program
# that intakes some words from the user and then generates a random password by jumbling those words.
import random


def numbers():      # Asking user how many numbers their password would have to increase security
    num = int(input("How many numbers would like in you password: "))
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    new_num = []
    for i in range(num):
        new_num.append(random.choice(number))

    return new_num  # Returning a random list of numbers based on the user's request


def special_chars():  # Asking user how many Special Characters their password would have to increase security
    spec_char = int(input("How many special characters would you like: "))
    sc = ['@', '#', '$', '%', '^', '&', '*', '+', '+', '_']
    new_char = []
    for i in range(spec_char):
        new_char.append(random.choice(sc))

    return new_char  # Returning a random list of Special Characters based on the user's request


def the_words():    # Asking the user for words, that would be used for the password
    words = input(str("Enter words: "))
    word_list = [words]     # words are stored as element in "word_list" list
    letters = []            # "letters" is a list that would contain each letter as an element from the word_list

    for i in word_list:
        for j in i:
            letters.append(j)
    for num in letters:     # Removing commas from the set
        if num == ',':
            letters.remove(',')

    return letters          # Returning the list of letters from the words


# --Main Code--
print("\nWelcome to Password Generator! Enter 2 words separated by a comma (,) ")

word = the_words()
nums = numbers()
spChars = special_chars()

jointList = word + nums + spChars       # Joining the three lists as one list

random.shuffle(jointList)               # Shuffling the Joint List
finalList = [x.strip(' ') for x in jointList]   # Removing any spaces (" ") the user might have written
finalList = ''.join(finalList)          # Concatenating individual elements in the list

print("\nYour Password is: ", finalList)        # Your new password!
