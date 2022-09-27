from tkinter import *

## 위젯에 대해서 공부

root = Tk()
root.title('Program1')
# root.geometry('640x480')

btn1 = Button(root, text='버튼1')
btn1.pack()

btn2 = Button(root, padx=5,pady=10, text='버튼2') # 버튼내의 크기 padx, pady// 버튼내의 여백
btn2.pack()
btn3 = Button(root, padx=20,pady=20, text='버튼3')
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # 버튼내 크기는 고정
btn4.pack()

btn5 = Button(root, fg='red', bg='yellow', text='버튼5') # 색을 지정
btn5.pack()

photo = PhotoImage(file='/Users/hyeonchanglee/Documents/data_analyst/005네이버쇼핑_키워드_순위추출프로그램/GUI/bot.png')
btn6 = Button(root,image=photo) # 불러온 이미지로 버튼을 만듬
btn6.pack()

def btncmd():
    print('버튼이 클릭되었습니다.')

btn7 = Button(root, text='동작하는 버튼', command=btncmd) # 버튼을 클릭시 함수를 실행
btn7.pack()



root.mainloop()