from tkinter import *

win = Tk() #창 생성
win.title("초코썬 과제")
win.geometry("1000x500+800+400") #가로*세로+x좌표+y좌표
win.option_add("*Font","맑은고딕 20")

def enter() :
    print("Photoshop2022를 실행합니다!")


menu = Menu(win) #1. 일단 메인메뉴바를 선언한다


#Adobe메뉴
menu_Adobe = Menu(menu, tearoff=0) #3. 하위메뉴를 만들고, 메인메뉴바에 이 하위 메뉴바가 속해있음을 알린다
menu_Adobe.add_command(label="Photoshop2022", command=enter) #4. 히위메뉴에 세부선택지를 add해준다
menu_Adobe.add_command(label="Illustrator2022")
menu_Adobe.add_separator()
menu_Adobe.add_command(label="PremierePro2022")
menu_Adobe.add_separator()
menu_Adobe.add_command(label="AdobeXD2021", state="disable") #비활성화 상태
menu_Adobe.add_separator()
menu_Adobe.add_command(label="Exit", command=win.quit) # win.quit = 프로그램 닫기

menu.add_cascade(label="Adobe", menu=menu_Adobe) #5. 하위메뉴menu_Adobe을 메인메뉴바에 add한다. Adobe이라는 이름으로! 


#Language (라디오버튼 통한 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="C++")  
menu_lang.add_radiobutton(label="Java")  
menu_lang.add_radiobutton(label="Python")
menu.add_cascade(label="Language", menu=menu_lang)  

#Show (체크박스 통한 다중선택)
menu_chk = Menu(menu, tearoff=0)
menu_chk.add_checkbutton(label="Show Minimap")
menu_chk.add_checkbutton(label="Show Entire map")
menu.add_cascade(label="Show", menu=menu_chk)


win.config(menu=menu) #2. 일단 그리고 해당 윈도우의 메뉴가 이 메뉴바에 있음을 알린다


win.mainloop() #창 실행