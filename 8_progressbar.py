import time 
import tkinter.ttk as ttk
from tkinter import *

win = Tk() #창 생성
win.title("초코썬 과제")
win.geometry("1000x500+800+400") #가로*세로+x좌표+y좌표
win.option_add("*Font","맑은고딕 20")


# progressbar1 = ttk.Progressbar(win, maximum=100, mode="indeterminate") #왔다갔다
# progressbar1.start(10) #10 ms마다 움직임
# progressbar1.pack()


# progressbar2 = ttk.Progressbar(win, maximum=100, mode="determinate")  #차오르기
# progressbar2.start(10) #10 ms마다 움직임
# progressbar2.pack()


# def btncmd(): 
#   progressbar1.stop() #작동중지
#   progressbar2.stop() 
 
# btn = Button(win, text="중지", command=btncmd)
# btn.pack()


p_var3 = DoubleVar() #실수 반영을 위해 더블바 연속적인값이기때문에!
progressbar3 = ttk.Progressbar(win, maximum=100, length=300, variable=p_var3)
progressbar3.pack()


def btncmd2(): 
  for i in range(1, 101) : # 1~100
      time.sleep(0.01) # 0.01초 대기
      p_var3.set(i) #progress bar의 값을 설정
      progressbar3.update() #매번 for문 동작 시마다 UI가 업데이트가 되게 해야 시각적으로 딜레이가 보인다!
      print(p_var3.get()) 

 
btn = Button(win, text="시작", command=btncmd2)
btn.pack()


win.mainloop() #창실행
