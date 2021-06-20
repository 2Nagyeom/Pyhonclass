from tkinter import *
import tkinter.messagebox as msgbox
import pyrebase

config = {
    "apiKey" : "AIzaSyBNfANylIvad__WX50a5p6c9GjT5WrE4bE",
    "authDomain" : "pyfriend-5cd0c.firebaseapp.com",
    "databaseURL" : "https://pyfriend-5cd0c-default-rtdb.firebaseio.com",
    "projectId" : "pyfriend-5cd0c",
    "storageBucket" : "pyfriend-5cd0c.appspot.com",
    "messagingSenderId" : "7021233597",
    "appId" : "1:7021233597:web:0b84298b6db1e5aa40bed4",
    "measurementId" : "G-10XX2QP7LN"
}

#데이터베이스 연동하기
firebase = pyrebase.initialize_app(config)
db=firebase.database()

#GUI 생성코드
window = Tk()
window.title("친구관리프로그램")
window.geometry('300x350')

l1 = Label(window , text="이름", width=10)
l1.grid(row=0, columnspan=1)

l2 = Label(window, text="전화번호", width=10)
l2.grid(row=1, column=0,pady=10)

l3 = Label(window, text="주소", width=10)
l3.grid(row=2, column=0,pady=10)

l4 = Label(window, text="이메일", width=10)
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


# 알림창 생성
def elart(msg):
    msgbox.showinfo("알림",msg)

# 마우스 이벤트 함수 생성

# 검색버튼 누르면 검색되는 함수 생성
def search():
    if (e1.get() == ''):
        elart('이름을 적어주세요')
    else:
        lb.delete('0', 'end')
        user = db.child("friends").child(e1.get()).get()
        print(user.val())
        lb.insert(END, user.val())
b1 = Button(f, text="검색", command=search)
b1.grid(row=4, column=0, padx=5)

#추가 버튼 누르면 추가되는 함수 생성
def add():
    lb.delete('0', 'end')
    data = {"0": e1.get() , "1":e2.get() , "2" : e3.get() , "3" : e4.get()}
    db.child("friends").child(e1.get()).set(data)
b2 = Button(f, text="추가", command=add)
b2.grid(row=4, column=1,padx=5)

#삭제 버튼 누르면 삭제되는 함수 생성
def delete():
    if(e1.get() == ''):
        elart('이름을 적어주세요')
    else :
        lb.delete('0', 'end')
        db.child("friends").child(e1.get()).remove()
        elart('삭제완료!')
b3 = Button(f, text="삭제", command=delete)
b3.grid(row=4, column=2, padx=5)

#수정 버튼 누르면 수정되는 함수 생성
def modi():
    if (e1.get() == ''):
        elart('이름을 적어주세요')
    else:
        lb.delete('0', 'end')
        db.child("friends").child(e1.get()).update({"1": e2.get(), "2": e3.get(), "3": e4.get()})
        elart('수정완료!')
b4 = Button(f, text="수정", command=modi)
b4.grid(row=4, column=3, padx=5)

#출력 버튼 누르면 출력되는 함수 생성
def pri():
    lb.delete('0', 'end')
    all_users = db.child("friends").get()
    for user in all_users.each():
        print(user.val())
        lb.insert(END, user.val())
b5 = Button(f, text="출력", command=pri)
b5.grid(row=4, column=4, padx=5)

#나가기 버튼 누르면 나가지는 함수 생성
def out():
    quit()
b6 = Button(f, text="종료", command=out)
b6.grid(row=4, column=5)

l = Frame(window)
l.grid(row=5, column=0, columnspan=2)

# 스크롤바 생성
scrollbar = Scrollbar(l)
scrollbar.grid(row=1, column=5)

lb = Listbox(l, bg="orange", yscrollcommand=scrollbar.set, border=0)
lb.grid(row=1,column=1)

scrollbar.config(command=lb.yview)
window.mainloop()