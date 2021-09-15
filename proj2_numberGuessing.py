import random

def greatThan(finput, number):
    if finput < number:
        print("The secret number is larger than", finput)
    elif finput > number:
        print("The secret number is smaller than", finput)

def multiple(number):
    if number % 3 == 0:
        print("the secret number is divisible by 3.")
    elif number % 5 == 0:
        print("the secret number is divisible by 5.")
    elif number % 7 == 0:
        print("the secret number is divisible by 7.")
    elif number % 11 == 0:
        print("the secret number is divisible by 11.")

def even(number):
    if number % 2 == 0:
        print("The secret number is an EVEN number!")
    else:
        print("The secret number is an ODD number!")

number = random.randint(1,30)
print(number)

finput = input("Guess a number between 1 to 30: ")

# score starts from 1 to unlimited

if finput == number:
    print("Good Job! You got it")
else:
    print("thats not it. Try again")
    for i in range(1,1000):
        i=i+1
        finput= int(input("\nGuess a number: "))
        if i == 2:
            greatThan(finput, number)

        elif i ==3:
            multiple(number)

        elif i ==4:
            print("Come on!")

        elif i == 5:
            even(number)
        elif i == 6:
            greatThan(finput, number)

        if finput == number:
            print("you got it.")
            print("number of tries: ", i)
            break
        else:
            print("Not it yet.")
