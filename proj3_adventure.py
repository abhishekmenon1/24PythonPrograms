def Room1(i):
    print(
        "\nYou have chose room 1 huh? There is one more door to enter to Win the game.\nThere is another door to go to Room 3 also. ")
    R1_1 = input('Which one do you pick? ENTER Door or R3: ')
    if R1_1 == 'Door':
        i = i + 1
        print("\nHAHAHAHA I was joking. You die!!!!!!")
        print("***Game Over***")
        print("No. of door entered: ", i)
    elif R1_1 == 'R3':
        Room3(i)
    else:
        print("\nBRUH! You should have picked one of the two options. Now get eaten by tarantulas.")
        print("***Game Over***")


def Room3(i):
    print("\nWelcome to Room 3, child. Now there is one door here where if you enter you could win.")
    R3_1 = input("ENTER Door to win: ")
    if R3_1 == 'Door':
        i = i + 1
        print("\nWOW you are gullible. YOU GET DEATH BY A BOREDOM!!!!")
        print("***Game Over***")
        print("No. of door entered: ", i)
    else:
        print("\nBRUH! You should have said Door. Now get cut by a saw.")
        print("***Game Over***")


def Room2(i):
    i = i + 1
    print("\nYou have entered Room 2. You now have three options.")
    print("ONE: To enter Room1 through a side door.")
    print("TWO: To run out of this room and enter into room3")
    print("THREE: Open the door that insects crawling out of it.")
    #R2_1 = input("Pick one. ENTER One or Two or Three")
    R3_1 = input("ENTER One or Two or Three to win: ")

    if R3_1 == 'One':
        i = i + 1
        Room1(i)


    elif R3_1 == 'Two':
        i = i + 1
        Room2(i)

    elif R3_1 == "Three":
        i = i + 1
        print("\nYou win! You sleazy ball of cheese")
        print("***Game Over***")
        print("No. of door entered: ", i)
    else:
        print("\nBRUH! You should have picked one of three options. Now eat some metal blades and die.")
        print("***Game Over***")

S1= input("Hello Little child! Welcome to the game of rooms. Do you wish to continue? ")
#for i in range(0,1000):
if S1 == 'YES' or S1=='yes' or S1 == 'Yes':
    print("\nSo you see three rooms in front of you.\nRoom 1 has broken wooden door.\nRoom 2 has a smudged grey door.\nRoom 3 has a golden shiny slab-gate as a door")
    S2 = input("Which room do you chose to enter? ENTER R1 or R2 or R3: ")
    i = 0
    if S2 == 'R1':
        i=i+1
        Room1(i)

    elif S2 == 'R2':
        i = i + 1
        Room2(i)

    elif S2 == 'R3':
        i = i + 1
        Room3(i)

    else:
        print("\nBRUH! You should have picked one of the three options. Now get eaten by sharks.")
        print("***Game Over***")

else:
    print("\nYou should've said yes. YOU HAVE CHOSEN DEAAAATTHHHH!!!! DIEE")
    print("***Game Over***")


