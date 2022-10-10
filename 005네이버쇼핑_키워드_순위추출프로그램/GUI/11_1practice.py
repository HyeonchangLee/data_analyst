from tkinter import *
import tkinter.messagebox as msgbox

## 위젯에 대해서 공부

root = Tk()
root.title('Program')
root.geometry('640x480+100+100') #가로x세로의 크기를 설정, + 이후로 가로 100, 세로 300으로 위치도 지정 가능

photo = PhotoImage(file='/Users/hyeonchanglee/Documents/data_analyst/005네이버쇼핑_키워드_순위추출프로그램/GUI/bot.png', height=50)

label_image = Label(root, image=photo).pack()
label1 = Label(root, text='네이버 키워드 저장 프로그램').pack()

def yesfunc():
   print('yes')

def nofunc():
   print('no')
btnyes = Button(root, text='예', command=yesfunc).pack()
btnno = Button(root, text='아니오', command=nofunc).pack()





root.mainloop()