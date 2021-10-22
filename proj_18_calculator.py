#Learnt from YouTuber Handy Mitial's Channel

import tkinter as tk

root = tk.Tk()
root. title("Calculator")
root.configure(bg = "light grey")
e_var= tk.StringVar()
expression = ''

display_Label = tk.Label(root, height= 5, width=60, textvariable=e_var, bg = "white", relief = 'sunken', font=(12))
display_Label.grid(row = 0, column = 0, rowspan = 3, columnspan = 4)

def button_Clicked(value):
    global expression
    global curr
    expression = expression + str(value)
    e_var.set(expression)

def button_clear():
    global expression
    e_var.set('')
    expression = ''

def button_delete():
    global expression

    expression = expression[:-1]
    e_var.set(expression)

def button_eval():
    global expression
    try:
        ans = eval(expression)
    except ZeroDivisionError:
        e_var.set("Can't divide with 0. Come on, you know better!")
    except:
        e_var.set("The expression doesn't seem right.")
    else:
        expression = f"{float(ans):,}"
        print("hehe")
        e_var.set(expression)
        curr1 = expression.replace(',','')
        expression = curr1


dic_function = {"1":lambda:button_Clicked(1), "2":lambda:button_Clicked(2), "3":lambda:button_Clicked(3), "4":lambda:button_Clicked(4), "5":lambda:button_Clicked(5), "6":lambda:button_Clicked(6), "7":lambda:button_Clicked(7),
                "8":lambda:button_Clicked(8), "9":lambda:button_Clicked(9), "0":lambda:button_Clicked(0), "C":button_clear, "<--":lambda:button_delete(),
                "=":button_eval, "+":lambda:button_Clicked('+'), '-':lambda:button_Clicked('-'), 'x':lambda:button_Clicked('*'), '/':lambda:button_Clicked('/'), '.':lambda:button_Clicked('.'),
                "(":lambda:button_Clicked("("), ")":lambda:button_Clicked(")")}

button_rows= [["7",'8','9','C'],['4','5','6','<--'],['1','2','3','x'],['0','.','-','+'],['(',')','/','=']]

for row_index, rows in enumerate(button_rows):
    for cell_index, cells in enumerate(rows):
        tk.Button(root, text = cells, command = dic_function.get(cells), width = 10, bg = "white", fg="red", font=("calibri bold",12)).grid(row = row_index + 3, column = cell_index)

root.mainloop()