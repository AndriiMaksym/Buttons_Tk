from tkinter import *
import tkinter


def on_button_one_click():
    print("Button One clicked!")


def on_button_second_click():
    print("Button Second clicked!")


top = tkinter.Tk()
top.title("Button App")

top.configure(bg="lightgray")

workspace_title = Label(
    text="Type of buttons", font=("Roboto", 24, "bold"), bg="lightgrey"
)
workspace_title.pack(pady=10)

top.geometry("400x400")

BT_ONE = tkinter.Button(
    top, text="Click me", relief=RAISED, command=on_button_one_click, width=15, height=3
)
BT_SECOND = tkinter.Button(
    top,
    text="Click me!!",
    relief=RAISED,
    command=on_button_second_click,
    width=15,
    height=3,
)

BT_ONE.pack(pady=10)
BT_SECOND.pack()

top.mainloop()
