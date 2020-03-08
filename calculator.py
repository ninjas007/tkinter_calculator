from tkinter import *

root = Tk()
root.title("Calculator")

# root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=r'/home/xyz/project_tkinter/calulator.ico'))

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# e.insert(0, "Enter Your Name: ")

def button_click(number):
	current_number = e.get()
	e.delete(0, END)
	e.insert(0, str(current_number) + str(number))

def button_add():
	current = e.get()
	global fnum
	global symbol
	fnum = int(current)
	symbol = "+"
	e.delete(0, END)

def button_minus():
	current = e.get()
	global fnum
	global symbol
	fnum = int(current)
	symbol = "-"
	e.delete(0, END)

def button_multiply():
	current = e.get()
	global fnum
	global symbol
	fnum = int(current)
	symbol = "x"
	e.delete(0, END)

def button_divide():
	current = e.get()
	global fnum
	global symbol
	fnum = int(current)
	symbol = "/"
	e.delete(0, END)

def button_equal():
	if symbol == "+":
		answer = fnum + int(e.get())

	if symbol == "-":
		answer = fnum - int(e.get())

	if symbol == "x":
		answer = fnum * int(e.get())

	if symbol == "/":
		answer = fnum / int(e.get())
	
	e.delete(0, END)
	e.insert(0, answer)

def button_clear():
	e.delete(0, END)

#  Define Buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_minus = Button(root, text="-", padx=39, pady=20, command=button_minus)
button_multiply = Button(root, text="x", padx=39, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=39, pady=20, command=button_divide)

button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_minus.grid(row=4, column=1)
button_multiply.grid(row=4, column=2)
button_divide.grid(row=6, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=6, column=1, columnspan=2)

# myButton = Button(root, text="Enter Your Stock Quote", command=myClick)

root.mainloop()