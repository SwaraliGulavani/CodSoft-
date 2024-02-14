import tkinter
from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()



window = Tk()

scvalue = StringVar()
scvalue.set("")

screen = Entry(window, textvar=scvalue, font="arial 30 bold")
screen.pack(fill=X,ipadx=8, padx=10, pady=10)
window.geometry("300x430")
window.title("Calculator")
window.config(background="black")


icon_path = "D:\Swarali\Calculator.png"
icon = tkinter.PhotoImage(file=icon_path)
window.iconphoto(False, icon)

f1 = Frame(window,background="#00E0C7")
b1 = Button(f1,text="C", font="arial 20 bold", padx=7, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=9, pady=5)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="%", font="arial 20 bold", padx=7, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=9, pady=5)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="*", font="arial 20 bold", padx=7, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=19, pady=5)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="/", font="arial 20 bold", padx=7, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=9, pady=5)
b1.bind("<Button-1>", click)
f1.pack()

f1 = Frame(window,background="#00E0C7")
b1 = Button(f1,text="7", font="arial 20 bold", padx=7, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=9, pady=5)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="8", font="arial 20 bold", padx=7, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=19, pady=5)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="9", font="arial 20 bold", padx=7, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=9, pady=5)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="-", font="arial 20 bold", padx=8, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=9, pady=5)
b1.bind("<Button-1>", click)
f1.pack()

f1 = Frame(window,background="#00E0C7")
b1 = Button(f1,text="4", font="arial 20 bold", padx=7, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=9, pady=5)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="5", font="arial 20 bold", padx=7, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=19, pady=5)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="6", font="arial 20 bold", padx=7, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=9, pady=5)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="+", font="arial 20 bold", padx=7, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=9, pady=5)
b1.bind("<Button-1>", click)
f1.pack()

f1 = Frame(window,background="#00E0C7")
b1 = Button(f1,text="1", font="arial 20 bold", padx=8, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=9, pady=5)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="2", font="arial 20 bold", padx=7, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=19, pady=5)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="3", font="arial 20 bold", padx=7, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=9, pady=5)
b1.bind("<Button-1>", click)
b1 = Button(f1,text=".", font="arial 20 bold", padx=8, pady=5, bg="black", fg="white")
b1.pack(side=LEFT, padx=9, pady=5)
b1.bind("<Button-1>", click)
f1.pack()

f1 = Frame(window,background="#00E0C7")
b1 = Button(f1,text="0", font="arial 20 bold", padx=2, pady=5, width = 9,bg="black", fg="white")
b1.pack(side=LEFT, padx=9, pady=5,)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="=", font="arial 20 bold", padx=5, pady=5, width = 4, bg="black", fg="white")
b1.pack(side=LEFT, padx=19, pady=5)
b1.bind("<Button-1>", click)
f1.pack()


window.mainloop()