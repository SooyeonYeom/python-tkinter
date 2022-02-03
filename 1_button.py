from tkinter import *

win = Tk() #창 생성
win.title("초코썬 과제")
#win.geometry("1000x500") #가로*세로
win.geometry("1000x500+800+400") #가로*세로+x좌표+y좌표


win.option_add("*Font","맑은고딕 25")


btn1 = Button(win, text="START!")
btn1.pack()

btn2 = Button(win, padx=10, pady=10, text="CLOSE") #글자 기준 패딩값 설정
btn2.pack()


btn3 = Button(win, padx=20, pady=20, text="OPEN") 
btn3.pack()


btn4 = Button(win, width=10, height=3, text="OPEN") #버튼 절대적 규격 설정
btn4.pack()




btn5 = Button(win, fg="skyblue", bg="yellow", text="OPEN") #버튼 글자색, 배경색 지정
btn5.pack()



def btncmd():
    print("버튼이 클릭되었어요!")

btn7 = Button(win, text="동작하는버튼", command=btncmd)  #버튼 동작시키기
btn7.pack() 



win.mainloop() #창 실행