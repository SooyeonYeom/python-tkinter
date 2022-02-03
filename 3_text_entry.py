from tkinter import *

win = Tk() #창 생성
win.title("초코썬 과제")
win.geometry("1000x500+800+400") #가로*세로+x좌표+y좌표
win.option_add("*Font","맑은고딕 20")

txt = Text(win, width=30, height=5) #줄바꿈 됨 (긴줄 가능)
txt.pack()
txt.insert(END, "글자를 입력하세요!")

e = Entry(win, width=30) #줄바꿈 안됨 (한줄용 짧은줄 가능)
e.pack()
e.insert(0,"한 줄만 입력하세요")



def btncmd(): 
    #내용 받아오기
    print(txt.get("1.0", END))
    print(e.get())

    #이후 텍스트 창에서 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(win, text="클릭", command=btncmd)
btn.pack()







win.mainloop() #창 실행