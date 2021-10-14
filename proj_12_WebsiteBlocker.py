"""
This is one of the useful python projects where you can build a program that blocks certain websites from opening.
This program is beneficial for students who want to study without any social media distractions.
"""

from tkinter import *

file_path = "------" #have not included. file path should lead you to "hosts" in System32
ipaddress = "-----" #have not included
def Block():
    info = web_name.get()
    host = open(file_path, "r")
    host_info = host.read()
    if info in host_info:
        print("Website already blocked")
        pass
    else:
        host_info.write(ipaddress + " " + info).place(200,200)

root = Tk()
root.title("Website Blocker")
root.geometry("400x200")
root.config(bg="orange")
root.columnconfigure(0, weight = 1)

#title label
title = Label(text = "Website Blocker", bg="orange", fg = "black", font=("calibri bold", 15))
title.grid()

#website blocker title
blocker = Label(text = "\nEnter Url",  bg="orange", fg = "black", font=("calibri bold", 10))
blocker.grid()

#website name

web_name = Entry(width = 50)
web_name.grid()
blocker = Label(text = "\n",  bg="orange", fg = "black", font=("calibri bold", 10))
blocker.grid()


#BLOCK Button
Block = Button(text="BLOCK", command = Block, font=("calibri bold", 10))
Block.grid()


root.mainloop()
