import tkinter.messagebox as msgbox
from tkinter import *

win = Tk() #창 생성
win.title("초코썬 과제")
win.geometry("1000x500+800+400") #가로*세로+x좌표+y좌표
win.option_add("*Font","맑은고딕 20")

#수강신청 시스템
def info() :
    msgbox.showinfo("알림","정상적으로 수강신청 완료되었습니다ㅎㅅㅎ!") #첫번째 값이 제목, 두번째 값이 안내문

def warn() :
    msgbox.showwarning("경고","해당 강좌의 정원이 초과되었습니다ㅠㅅㅠ!") #첫번째 값이 제목, 두번째 값이 안내문

def error() :
    msgbox.showerror("에러","정보화본부가 일을 안합니다!") #첫번째 값이 제목, 두번째 값이 안내문

def OKcancel() :
    msgbox.askokcancel("확인 / 취소","해당 강좌는 로드가 개빡셉니다. 수강하시겠습니까?") #msgbox.askokcancel로 [확인/취소]를 물어볼 수 있다!
     
def retrycancel() :
    msgbox.askretrycancel("재시도 / 취소","일시적인 오류입니다. 다시 시도하시겠습니까?") #msgbox.askretrycancel로 [재시도/취소]를 물어볼 수 있다!
     
def yesno() :
    msgbox.askyesno("예 / 아니오","해당 강좌는 전남친이 있습니다. 수강하시겠습니까?") #msgbox.askyesno로 [예/아니오]를 물어볼 수 있다!

def yesnocancel() :
    response = msgbox.askyesnocancel("예 / 아니오 / 취소", "수강신청이 완료되지 않았습니다. \n완료 후 프로그램을 종료하시겠습니까?")  #msgbox.askyesnocancel로 [예/아니오/취소]를 물어볼 수 있다!
     #예 : 저장 후 종료 True=1
     #아니오 : 저장 하지 않고 종료 False=0
     #취소 : 프로그램 종료 취소 (현재화면에서 계속 작업) None=취소
    print("응답:", response) 
    if response == 1: 
        print("예")
    elif response == 0:
        print("아니오")
    else :
        print("취소")
     
#사용자로부터 값을 받기위해 메시지박스 함수 앞에 response를 붙인 후, 그 아래 if문으로 각 응답에 해당하는 출력값을 지정해주면 된다! 

Button(win, command=info, text="알림").pack()

Button(win, command=warn, text="경고").pack()

Button(win, command=error, text="에러").pack()


Button(win, command=OKcancel, text="확인 취소").pack()
Button(win, command=retrycancel, text="재시도 취소").pack()
Button(win, command=yesno, text="예 아니오").pack()
Button(win, command=yesnocancel, text="예 아니오 취소").pack()


win.mainloop() #창 실행