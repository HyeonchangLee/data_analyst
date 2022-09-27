from tkinter import *

## 위젯에 대해서 공부

root = Tk()
root.title('Program1')
root.geometry('640x480')


chkvar = IntVar() #chkvar의 Int형으로 데이터를 저장
chkbox = Checkbutton(root,text='오늘 하루 보지 않기',variable=chkvar) # variable로 체크의 값을 어떤 변수에 저장해서 가져옴, 
# chkbox.select() # 자동 선택처리
# chkbox.deselect() # 자동 선택 해제처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text='일주일 동안 보지 않기', variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 체크박스의 값을 가져옴, 0일경우 체크 해제, 1은 체크됨을 의미
    print(chkvar2.get()) # 체크박스의 값을 가져옴, 0일경우 체크 해제, 1은 체크됨을 의미


btn = Button(root, text='click', command=btncmd)
btn.pack()

root.mainloop()