from tkinter import *

window = Tk()

l1 = Label(window , text="이름")
l1.grid(row=0, column=0)

l2 = Label(window, text="전화번호")
l2.grid(row=1, column=0,pady=10)

l3 = Label(window, text="주소")
l3.grid(row=2, column=0,pady=10)

l4 = Label(window, text="이메일")
l4.grid(row=3, column=0,pady=10)

e1 = Entry(window, bg="orange")
e1.grid(row=0, column=1)

e2 = Entry(window,bg="orange")
e2.grid(row=1, column=1)

e3 = Entry(window,bg="orange")
e3.grid(row=2, column=1)

e4 = Entry(window,bg="orange")
e4.grid(row=3, column=1)

f = Frame(window)
f.grid(row=4, column=0, columnspan=2)

b1 = Button(f, text="검색")
b1.grid(row=4, column=0, padx=8)

b2 = Button(f, text="추가")
b2.grid(row=4, column=1,padx=8)

b3 = Button(f, text="삭제")
b3.grid(row=4, column=2, padx=8)

b4 = Button(f, text="수정")
b4.grid(row=4, column=3, padx=8)

b5 = Button(f, text="종료")
b5.grid(row=4, column=4)

lb = Listbox(window, height=10, width=20, bg="orange", border=0)
lb.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()