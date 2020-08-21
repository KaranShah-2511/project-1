import math, random
from tkinter import *
import tkinter.messagebox

new = Tk()
new.title("LUCK GAME")

e1l = Label(new, text = "Enter Player Name")
e1l.pack()
e1=Entry(new)
e1.pack()
Rules = Label(new , text = "\n\nRules: \n\nStep 1) Enter Your Name. \n\n Syep 2)Press create Button .\n\n Step 3) Enter your Number between\n 1 to 10. \n\n Step 4) Press ok Button")
Rules.pack()
new.geometry("300x300+600+300")
S_button = Button(new, text=" Start", command=new.destroy).pack()




new.mainloop()

gen_number = ''
urs_number = ''


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def create():
    otp = random.randint(1, 10)
    print("Genreated Number is: ", otp)
    global gen_number
    gen_number = otp


def g_n():
    return gen_number


def u_n():
    return urs_number


def ok():
    first_number = e.get()

    global f_num
    global urs_number
    f_num = int(first_number)
    urs_number = f_num
    print("User Number is: ", urs_number)
    if g_n() == u_n():
        print("win")
        tkinter.messagebox.showinfo("RESULT!", "You Win")
        e.delete(0, END)
        return create()

    else:
        print("loss")
        tkinter.messagebox.showinfo("RESULT!", "You Loss")
        e.delete(0, END)
        return create()


def clear():
    e.delete(0, END)


def close():
    quit()


root = Tk()
root.geometry("300x300+600+300")
root.title("LUCK GAME")

e = Entry(root, width=25, borderwidth=5)
# e.grid(row=0, column=0, padx=5,pady=5,ipady=15)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

a = Entry(root, width=8, borderwidth=3)
a.grid(row=2, column=3, columnspan=5, padx=10, pady=10)

# create Button


button_1 = Button(root, text="1", padx=20, pady=5, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=5, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=5, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=5, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=5, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=5, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=5, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=5, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=5, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=5, command=lambda: button_click(0))
button_clear = Button(root, text="Clear", padx=15, pady=10, command=clear)
button_create = Button(root, text="crate", padx=15, pady=10, command=create)
button_ok = Button(root, text="ok", padx=20, pady=10, command=ok)
button_close = Button(root, text="close", padx=20, pady=10, command=close)
Amount = Label(root, text="Enter Amount").grid(row=1, column=5)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_create.grid(row=4, column=2)
button_ok.grid(row=5, column=0)
button_close.grid(row=5, column=2)

root.mainloop()
