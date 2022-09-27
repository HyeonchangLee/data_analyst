from tkinter import *

## 위젯에 대해서 공부

root = Tk()
root.title('Program1')

#레이블은 글자나 이미지만 보여줌

label1 = Label(root, text='안녕하세여')
label1.pack() # 실행

photo = PhotoImage(file='/Users/hyeonchanglee/Documents/data_analyst/005네이버쇼핑_키워드_순위추출프로그램/GUI/bot.png')
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text='text  changed')  # 버튼을 누르면 텍스트를 바꾸는 함수

    global photo2
    photo2 = PhotoImage(file='/Users/hyeonchanglee/Documents/data_analyst/005네이버쇼핑_키워드_순위추출프로그램/GUI/x.png')
    label2.config(image=photo2)

btn = Button(root, text='click', command=change)
btn.pack()


root.mainloop()