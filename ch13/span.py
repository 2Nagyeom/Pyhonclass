from tkinter import *

window = Tk()

Label(window, text="λλΉ").grid(row=0)
Label(window, text="λμ΄").grid(row=1)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Label.grid(row=0, column=2, columnspan=2, rowspan=2)

window.mainloop()