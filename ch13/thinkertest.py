from tkinter import *

# root window 생성
window = Tk()
window.geometry("400x300")
window.title("tkinder test")


l1 = Label(window, text="이름")
# pack은 압축배치관리름
l1.pack(side=LEFT)

l2 = Label(window, text="전화번")
l2.pack(side=TOP)

l3 = Label(window, text="주소")
l3.pack(side=BOTTOM)

l4 = Label(window, text="이메일")
l4.pack(side=RIGHT)


window.mainloop()