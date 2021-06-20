from tkinter import *

window = Tk()
window.geometry("400X300")
counter = 0;

def clicked():
    global counter
    counter += 1
    label['Text'] = '버튼 클릭 횟수:' + str(counter)

label = Label(window,text="아직 눌러지지 않음")
label.pack()
button = Button(window, text="증가", command=clicked).pack()

window.mainloop()