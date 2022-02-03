from tkinter import *

win = Tk() #창 생성
win.title("초코썬 과제")
win.geometry("1000x500+800+400") #가로*세로+x좌표+y좌표
win.option_add("*Font","맑은고딕 20")


frame = Frame(win)
frame.pack()

sbar = Scrollbar(frame)
sbar.pack(side="right", fill="y")

#set이 없으면 스크롤을 내려도 다시 올라옵니다
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=sbar.set) #리스트박스를 스크롤바에 매핑하기
for i in range(1,32): #1부터 31까지
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")

sbar.config(command=listbox.yview) #스크롤바를 리스트박스에 매핑하기 ##서로 매핑해줌으로서 기능이 상호작용된다!



win.mainloop() #창 실행