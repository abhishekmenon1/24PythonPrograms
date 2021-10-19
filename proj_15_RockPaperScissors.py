import random


def user_move(user_play):   #this function is used to verfiy if the user input is either R,S or P
    if user_play == 'R' or user_play == 'P' or user_play == 'S':
        return True
    else:
        return False

def rando():    #this function randomly picks Rock, Paper or Scissors.
                # There is an extra "Rock" in the options set to make the program's guess slightly more predictable
    options=("Rock", "Paper", "Scissor", "Rock")
    opt = random.choice(options)
    return opt

def game(user_play, computer_choice):   #this function defines the rules of the game
    user = user_play
    computer = computer_choice

    if user == "R" and computer == "Paper":
        result = "--Computer Wins--"
        winner = "computer"
        return result, winner
    elif user == "R" and computer == "Scissor":
        result = "--You Win--"
        winner = "user"
        return result, winner

    elif user == "P" and computer == "Rock":
        result = "--You Win--"
        winner = "user"
        return result, winner
    elif user == "P" and computer == "Scissor":
        result = "--Computer Wins--"
        winner = "computer"
        return result, winner

    elif user == "S" and computer == "Rock":
        result = "--Computer Wins--"
        winner = 'computer'
        return result, winner
    elif user == "S" and computer == "Paper":
        result = "--You Win--"
        winner = "user"
        return result, winner

    else:
        result = "--Draw. No points--"
        winner = "none"
        return result, winner


print("\nWelcome to Rock, Paper..... and .... Scissors!")
print("To play, enter\n'R' for ROCK\n'P' for PAPER\n'S' for SCISSORS")
inp1 = input("Wanna Play? ")

if inp1 == "yes" or inp1 =="yeah" or inp1 =="Yes" or inp1 =="YES" or inp1 =="Yeah" or inp1 == "y" or inp1 == "Y":
   #used to get the initial value "YES" from the user to start the game
    print("\nSo.. its a play of 7.")
    user_points = 0

    comp_points = 0

    for i in range(1,8):
        print("Play:",i)
        user_play = input("Your move: ").upper()
        if user_move(user_play):
            computer_choice = rando()
            print("Computer choice: ", computer_choice)
            result,winner = game(user_play, computer_choice)
            print(result)
            if winner == "user":
                user_points = user_points + 1

            if winner == "computer":
                comp_points = comp_points + 1

            print("\nUser Score:", user_points, " || Computer Score: ", comp_points)

        else:
            print("Invalid entry. Try again.\n")
            user_play = input("Your move: ").upper()

    if user_points > comp_points:
        print("--- YOU WIN THE GAME, CONGRATS!! ---")
    elif comp_points > user_points:
        print("--- THE COMPUTER WINS THE GAME. TRY AGAIN AND BEAT IT!! ---")
    else:
        print("--- DRAW GAME! WHAT WERE THE CHANCES! ---")

else:
    print("\nBbye!")