from tkinter import *

def check():    #this function does the backend work of the leap year button. THe user input is categorised into century based (100,1800 etc) and others(1999,2012 etc)
    the_tens = 0
    other = 0

    user = user_input.get()
    if user % 100 == 0:
        the_tens = user
        print("Tens= ", the_tens)
    else:
        other = user
        print("others= ",other)
    if the_tens > 1 and other == 0: #either the_tens aka century years would be have the year or other aka non-ten years would have a number
        if the_tens % 400 == 0:
            the_text.config(text="\nIT IS A LEAP YEAR!", fg="green", font=("calibri bold", 14))
        else:
            the_text.config(text="\nNOT A LEAP YEAR!", fg="red", font=("calibri bold", 14))
    if the_tens == 0 and other > 1:
        if other % 4 == 0:
            the_text.config(text="\nIT IS A LEAP YEAR!", fg="green", font=("calibri bold", 14))
        else:
            the_text.config(text="\nNOT A LEAP YEAR!", fg="red", font=("calibri bold", 14))

root = Tk() #tkinter root
root.title("Leap Year")
root.geometry("400x300")
root.columnconfigure(0, weight = 1)

Title = Label(root, text="Leap Year!\n", font = ("calibri", 18))
Title.grid()

user_input = IntVar()
user_box = Entry(root, width = 20, text = user_input)
user_box.grid()

Title = Label(root, text="(Enter Year)\n", fg ="red", font = ("calibri", 10))
Title.grid()

Button = Button(root, text = "Check Year", bg = "red", fg = "white", command=check, font = ("calibri", 12))
Button.grid()

the_text = Label(root, text="\n", fg = "black", font=("calibri", 12))
the_text.grid()

root.mainloop()