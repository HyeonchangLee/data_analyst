from tkinter import *

## 위젯에 대해서 공부

root = Tk()
root.title('Program1')
root.geometry('640x480')

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand=scrollbar.set) #yscrollcommand=scrollbar.set로 리스트박스에 스크롤을 매핑해줌

for i in range(1,32): #1~31일의 정보를 리스트 박스에 넣음
    listbox.insert(END, str(i) + '일') # insert는 데이터를 삽입, END는 끝까지, 1일~ 31일까지를
listbox.pack(side='left')

scrollbar.config(command=listbox.yview) # listbox를 매핑해서 잡아줌

root.mainloop()

