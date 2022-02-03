from tkinter import *

win = Tk() #창 생성
win.title("초코썬 과제")
win.geometry("1000x500+800+400") #가로*세로+x좌표+y좌표
win.option_add("*Font","맑은고딕 20")


# btn1 = Button(win, text="버튼1")
# btn2 = Button(win, text="버튼2")

# #btn1.pack()
# #btn2.pack()

# # btn1.pack(side="left")
# # btn2.pack(side="right")

# # btn1.pack(side="left")
# # btn2.pack(side="left")

# btn1.grid(row=0, column=0) #X=행=row / Y=열=column
# btn2.grid(row=1, column=1) #X=행=row / Y=열=column  


#grid로 행과열을 설정, sticky라는 속성으로 주변 객체로 늘려주기 가능!
#버튼에 패딩값 줘서 각 버튼을 조정할 수 있다
#그리드에 패딩값을 줘서 각 객체의 사이값을 조정할 수 있다
#cmd+c로 범위 설정 > cmd+f로 찾기 : 여기서 한번에 조정 가능!


# 첫번째 줄
btn_f16 = Button(win, text="f16", padx=10, pady=10)
btn_f17 = Button(win, text="f17")
btn_f18 = Button(win, text="f18")
btn_f19 = Button(win, text="f19")

btn_f16.grid(row=0,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0,column=3, sticky=N+E+W+S, padx=3, pady=3)


# 두번째 줄 
btn_clear = Button(win, text="clear", padx=10, pady=10)
btn_equal = Button(win, text="=")
btn_div = Button(win, text="/")
btn_mul = Button(win, text="*")

btn_clear.grid(row=1,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1,column=3, sticky=N+E+W+S, padx=3, pady=3)


# 세번째 줄 
btn_7 = Button(win, text="7", padx=10, pady=10)
btn_8 = Button(win, text="8")
btn_9 = Button(win, text="9")
btn_min = Button(win, text="-")

btn_7.grid(row=2,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_min.grid(row=2,column=3, sticky=N+E+W+S, padx=3, pady=3)


# 네번째 줄 
btn_4 = Button(win, text="4", padx=10, pady=10)
btn_5 = Button(win, text="5")
btn_6 = Button(win, text="6")
btn_add = Button(win, text="+")

btn_4.grid(row=3,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3,column=3, sticky=N+E+W+S, padx=3, pady=3)



# 다섯번째 줄 
btn_1 = Button(win, text="1", padx=10, pady=10)
btn_2 = Button(win, text="2")
btn_3 = Button(win, text="3")
btn_enter = Button(win, text="enter") #세로로 합쳐져야함

btn_1.grid(row=4,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4,column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) #rowspan=현재 위치로부터 아래쪽으로 몇 줄을 더함 


# 마지막 줄 
btn_0 = Button(win, text="0", padx=10, pady=10) #가로로 합쳐져야함
btn_point = Button(win, text=".")

btn_0.grid(row=5,column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3) #columnspan=현재 위치로부터 오른쪽으로 몇 칸 더함 
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)




win.mainloop() #창 실행