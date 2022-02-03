from tkinter import *

win = Tk() #창 생성
win.title("초코썬 과제")
win.geometry("1000x500+800+400") #가로*세로+x좌표+y좌표
win.option_add("*Font","맑은고딕 20")

chkvar = IntVar() #chkvar에 int형으로 값을 저장한다 
chkbox = Checkbutton(win, text="오늘 하루 보지 않기", variable=chkvar)
#chkbox.select() #기본선택처리
#chkbox.deselect() #선택해제처리
chkbox.pack()

chkvar2 = IntVar() #chkvar에 int형으로 값을 저장한다 
chkbox2 = Checkbutton(win, text="일주일동안 보지 않기", variable=chkvar2)
#chkbox2.select() #기본선택처리
#chkbox2.deselect() #선택해제처리
chkbox2.pack()



def btncmd(): 
   print(chkvar.get())  # 값이 '0'으로 출력되면 체크 해제 / 값이 '1'로 출력되면 체크 상태
   print(chkvar2.get())  # 값이 '0'으로 출력되면 체크 해제 / 값이 '1'로 출력되면 체크 상태

btn = Button(win, text="클릭", command=btncmd)
btn.pack()







win.mainloop() #창 실행