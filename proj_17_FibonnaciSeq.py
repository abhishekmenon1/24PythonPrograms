from tkinter import *

def check():
    user = User_Input.get()
    sum = 0
    while sum <= user:
        k = [0,1]
        for j in range(0,100):
            sum = k[j+1] + k[j]
            k.append(sum)
            if k[j] == user:
                Answer.config(text= "\nYes, Fibonnaci Sequence!", fg = "green", font = ("calibiri bold", 12))
                seq.config(text = k)
                break
            else:
                Answer.config(text = "\nNot a fibonnaci number :(", fg = "red", font = ("calibiri bold", 12))
                seq.config(text="")

root = Tk()
root.title("Fibonnaci Checker")
root.geometry("600x300")
root.columnconfigure(0, weight = 1)
root.configure(background = "Pink")

Title = Label(root, text = "\nFibonnaci Sequence", fg = "Black", bg="Pink", font=("calibiri bold", 14))
Title.grid()

Space = Label(root, text = "\n", bg="Pink", font=("calibiri bold", 14))
Space.grid()

User_Input = IntVar()
box = Entry(root, width = "30", text=User_Input)
box.grid()

inst = Label(root, text = "(Enter Number)", bg = "pink", font=("calibiri bold", 8))
inst.grid()

Space = Label(root, text = "\n", bg="Pink", font=("calibiri bold", 14))
Space.grid()

button = Button(root, width = "20", command = check, text = "Check!", bg = "white", fg ="green", font=("calibiri bold", 12))
button.grid()

Answer = Label(root, text= "", bg ="pink", font=("calibiri bold", 12))
Answer.grid()

seq = Label(root, text= "", bg ="pink", font=("calibiri bold", 10))
seq.grid()

root.mainloop()
