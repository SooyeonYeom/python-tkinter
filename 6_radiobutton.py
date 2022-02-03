from tkinter import *

win = Tk() #창 생성
win.title("초코썬 과제")
win.geometry("1000x500+800+400") #가로*세로+x좌표+y좌표
win.option_add("*Font","맑은고딕 20")


label1 = Label(win, text="오늘 할 운동은 무엇인가요?")
label1.pack()


burger_var = IntVar() #여기에 Int형으로 값을 저장한다
btn_burger1 = Radiobutton(win, text="등", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(win, text="가슴", value=2, variable=burger_var)
btn_burger3 = Radiobutton(win, text="어깨", value=3, variable=burger_var)
btn_burger3 = Radiobutton(win, text="하체", value=4, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()



label2 = Label(win, text="오늘 먹을 단백질은 무엇인가요?")
label2.pack()

protein_var = StringVar() 
btn_protein1 = Radiobutton(win, text="닭가슴살", value="닭가슴살", variable=protein_var)
btn_protein1.select()
btn_protein2 = Radiobutton(win, text="우둔살", value="우둔살", variable=protein_var)
btn_protein3 = Radiobutton(win, text="삶은계란", value="삶은계란", variable=protein_var)

btn_protein1.pack()
btn_protein2.pack()
btn_protein3.pack()




def btncmd(): 
  print(burger_var.get()) # 선택지 중 선택된 라디오 항목의 value을 get하는 것!
  print(protein_var.get()) 

btn = Button(win, text="오늘은 여길 조질겁니다", command=btncmd)
btn.pack()







win.mainloop() #창 실행