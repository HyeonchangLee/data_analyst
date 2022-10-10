from tkinter import *
import tkinter.ttk as ttk


## 위젯에 대해서 공부

root = Tk()
root.title('Program1')
root.geometry('640x480')


values = [str(i) + '일' for i in range(1,32)] # 1~31까지의 날짜
combobox = ttk.Combobox(root, height=5, values=values) # state는 값을 넣지 못하게
combobox.set('카드 결제일') # 처음 떳을 경우의 텍스트를 출력
combobox.pack()

r_combobox = ttk.Combobox(root, height=10, values=values, state='readonly') # state는 값을 넣지 못하게 상태를 변경 가능
r_combobox.current(0) # 0번쨰 인덱스 값 설정
r_combobox.pack()

def btncmd():
   print(combobox.get()) # 선택된 값 표시
   print(r_combobox.get()) # 선택된 값 표시

btn = Button(root, text='select', command=btncmd)
btn.pack()

root.mainloop()