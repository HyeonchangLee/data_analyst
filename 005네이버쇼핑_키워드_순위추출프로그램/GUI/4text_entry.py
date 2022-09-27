from tkinter import *

## 위젯에 대해서 공부

root = Tk()
root.title('Program1')
root.geometry('640x480')

txt = Text(root, width=30, height=5) # 텍스트창 생성, 여러줄로 입력 (텍스트)
txt.pack()

txt.insert(END, '글자를 입력하세요') #기본값의 텍스트를 출력

e = Entry(root, width=30) # 한줄로만 입력받을 때(엔트리)
e.pack()
e.insert(0,'g')


def btncmd():
    print(txt.get('1.0',END)) # 1.0 첫번째 라인의 0번째 컬럼위치 부터 END 마지막 까지 가져옴 (텍스트 창의 모든 글자를 가져옴)
    print(e.get())# 엔트리에 쓴 모든 글자를 가져옴 

    txt.delete('1.0',END) # 처음부터 끝까지의 텍스트의 내용을 삭제
    e.delete(0, END)# 처음부터 끝까지의 엔트리의 내용을 삭제

btn = Button(root, text='click', command=btncmd)
btn.pack()

root.mainloop()