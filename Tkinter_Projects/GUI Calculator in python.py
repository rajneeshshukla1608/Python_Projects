from tkinter import *
from tkinter.messagebox import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    position = screen.index(INSERT)

    # Changing position of cursor one character right
    screen.icursor(position + 1)

    # print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())  # it evaluate the string values
            except Exception as e:
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()

root.geometry("290x375")
root.resizable(0, 0)

root.title("Calculator - Rajneesh Shukla")
root.wm_iconbitmap("notepad.ico")
scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 20 bold")
screen.pack(ipadx=15, padx=10, pady=10)
screen.focus()
f = Frame(root, bg="grey")
b = Button(f, text="9", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="6", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="5", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="3", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")

b = Button(f, text="1", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="0", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", font="lucida 17 bold", padx=9, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="*", font="lucida 15 bold", padx=9, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="/", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="C", font="lucida 15 bold", padx=10, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")

b = Button(f, text=".", font="lucida 15 bold", padx=9, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="00", font="lucida 15 bold", padx=9, pady=5)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", font="lucida 15 bold", padx=10, pady=5, width=7)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)



f.pack()

root.mainloop()