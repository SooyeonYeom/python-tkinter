from tkinter import *

win = Tk() #창 생성
win.title("초코썬 과제")
win.geometry("1000x500+800+400") #가로*세로+x좌표+y좌표

win.option_add("*Font","맑은고딕 20")

label1 = Label(win, text="Zzz..Zzz..")
label1.pack()


photo1 = PhotoImage(file="GUI/Asset1.png")

photo2 = PhotoImage(file="GUI/Asset2.png")



def change() :
    btn.config(image=photo2)
    label1.config(text="읏챠! 좋은 아침~!")


btn = Button(win, image=photo1, command=change)
btn.pack()


win.mainloop() #창 실행