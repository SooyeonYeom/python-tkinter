from tkinter import *

win = Tk() #창 생성
win.title("초코썬 과제")
win.geometry("1000x500+800+400") #가로*세로+x좌표+y좌표
win.option_add("*Font","맑은고딕 20")


listbox = Listbox(win, selectmode="extended", height=0) #셀렉모드를 single = 단일선택, extended = 중복선택 ##height는 0이라두면 선택지 전부 보이지만, 정수로 지정하면 해당 정수값만큼만 리스트 1면에 보인다
listbox.insert(0, "포뇨")
listbox.insert(1, "초코")
listbox.insert(2, "곰돌")
listbox.insert(END, "레몬")
listbox.insert(END, "모찌")
listbox.pack()




def btncmd(): 
   #리스트 목록 삭제
   #listbox.delete(END) #0이면 처음부터, END면 뒤에서부터

   #리스트 총 갯수 확인
   #print("리스트에는", listbox.size(), "개가 있어요")

   #특정 항목 받아오기 get(시작인덱스,끝인덱스)
   #print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2)) #리스트박스에서, 가져와라, 0부터 2까지의 값을!

   #선택된 항목 받아오기 (인덱스 위치값로 표현 ex. (1,2,3) )
   print("선택된 항목 : ", listbox.curselection())  #current selection = 현재 선택된 항목 


btn = Button(win, text="클릭", command=btncmd)
btn.pack()







win.mainloop() #창 실행