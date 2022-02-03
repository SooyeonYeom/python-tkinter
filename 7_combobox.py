import tkinter.ttk as ttk
from tkinter import *

win = Tk() #창 생성
win.title("초코썬 과제")
win.geometry("1000x500+800+400") #가로*세로+x좌표+y좌표
win.option_add("*Font","맑은고딕 20")


values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31까지의 숫자
combobox = ttk.Combobox(win, height=5, values=values)
combobox.pack()
combobox.set("당신이 태어난 날은?") #제목 설정 or 버튼 클릭을 통한 값설정



values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31까지의 숫자
combobox2= ttk.Combobox(win, height=10, values=values, state="readonly") #사용자가 수정 불가, 읽기만 할 수 있는 상태로 고정 #height로 리스트가 얼만큼 보이게 할지 조정
#combobox2.current(0) #0번째 인덱스값 선택 
combobox2.set("당신이 제일 좋아하는 날은?") #제목 설정
combobox2.pack()



def btncmd(): 
  print(combobox.get()) #선택된 값 표시
  print(combobox2.get())

btn = Button(win, text="선택", command=btncmd)
btn.pack()

win.mainloop() #창실행
