from tkinter import *

## 위젯에 대해서 공부

root = Tk()
root.title('Program1')
root.geometry('640x480')

Label(root,text='메뉴를 선택해 주세요.' ).pack(side='top')
Button(root, text='주문하기').pack(side='bottom')

frame_burger = Frame(root,relief='solid', bd=1) # relief 테두리 모양, bd 외곽선
frame_burger.pack(side='left',fill='both',expand=True) #side는 어느 위치에 넣을지, fill은 양쪽 채우기, expand는 넓히기

Button(frame_burger, text='햄버거').pack()
Button(frame_burger, text='치즈버거').pack()
Button(frame_burger, text='치킨버거').pack()

frame_drink = LabelFrame(root, text='음료')
Button(frame_drink, text='콜라').pack()
Button(frame_drink, text='사이다').pack()
frame_drink.pack(side='right', fill='both',expand=True)


root.mainloop()
