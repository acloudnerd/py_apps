from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# labelling

entry = Entry(width=10)
entry.pack(side="top")


def button_clicked():
    output = entry.get()
    my_label = Label(text=output, font=("Arial", 34, "italic"))
    my_label.pack(expand=1)


button = Button(text="Click Me", command = button_clicked)
button.pack(side="top")


window.mainloop()

# def add(*args):
#     print(sum(args))


# add(1,2,3,4,5,6,7,8,9,10)
