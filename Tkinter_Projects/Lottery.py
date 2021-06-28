from tkinter import *
from random import sample

window = Tk()
window.title("Lottery Game")
window.resizable(0, 0)

img = PhotoImage(file="lottery.png")

imgLabel = Label(window, image=img)
label1 = Label(window, relief=GROOVE, width=3, height=1, text="...")
label2 = Label(window, relief=GROOVE, width=3, height=1, text="...")
label3 = Label(window, relief=GROOVE, width=3, height=1, text="...")
label4 = Label(window, relief=GROOVE, width=3, height=1, text="...")
label5 = Label(window, relief=GROOVE, width=3, height=1, text="...")

getbtn = Button(window)
resbtn = Button(window)

imgLabel.grid(row=1, column=1, rowspan=2)
label1.grid(row=1, column=2, padx=10)
label2.grid(row=1, column=3, padx=10)
label3.grid(row=1, column=4, padx=10)
label4.grid(row=1, column=5, padx=10)
label5.grid(row=1, column=6, padx=10)

getbtn.grid(row=2, column=2, columnspan=4)
resbtn.grid(row=2, column=5, columnspan=2)

getbtn.configure(text="Get the lucky number")
resbtn.configure(text="Reset")

resbtn.configure(state=DISABLED)


def pick():
    nums = sample(range(1, 20), 6)
    label1.configure(text=nums[0])
    label2.configure(text=nums[1])
    label3.configure(text=nums[3])
    label4.configure(text=nums[4])
    label5.configure(text=nums[5])
    getbtn.configure(state=DISABLED)
    resbtn.configure(state=NORMAL)


def reset():
    label1.configure(text="...")
    label2.configure(text="...")
    label3.configure(text="...")
    label4.configure(text="...")
    label5.configure(text="...")
    getbtn.configure(state=NORMAL)
    resbtn.configure(state=DISABLED)


getbtn.configure(command=pick)
resbtn.configure(command=reset)

window.mainloop()