from tkinter import *

win = Tk() #창 생성
win.title("초코썬 과제")
win.geometry("1000x500+800+400") #가로*세로+x좌표+y좌표
win.option_add("*Font","맑은고딕 20")


Label(win, text="운동과 식단을 선택해주세요!").pack(side="top")

Button(win, text="주문하기").pack(side="bottom")


#단백질프레임
frame_protein = LabelFrame(win, relief="solid", bd=1, text="단백질")
frame_protein.pack(side="left", fill="both", expand=True) #패키징에 옵션 추가해서 프레임모양을 바꿀 수 있다

Button(frame_protein, text="닭가슴살").pack()
Button(frame_protein, text="우둔살").pack()
Button(frame_protein, text="삶은 계란").pack()

#운동프레임
frame_exercise = LabelFrame(win, relief="solid", bd=1,text="운동")
frame_exercise.pack(side="right", fill="both", expand=True)

Button(frame_exercise, text="가슴").pack()
Button(frame_exercise, text="등").pack()
Button(frame_exercise, text="어깨").pack()


win.mainloop() #창 실행