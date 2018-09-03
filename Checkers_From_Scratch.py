
import tkinter as tk

window = tk.Tk()

window.title("Checkers")

window.geometry("400x400")

# LABEL
title = tk.Label(text="Hello world")
title.grid(column=0, row=0)

# Button
button1 = tk.Button(text="Click me!")
button1.grid(column=0, row=1)


# Entry field
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)


window.mainloop()

