from tkinter import *
import tkinter.ttk as ttk
import time

## 위젯에 대해서 공부

root = Tk()
root.title('Program1')
root.geometry('640x480')

# progressbar = ttk.Progressbar(root, maximum=100, mode= 'indeterminate') # 맥시멈 값을 설정, indeterminate는 결정되지않음.
# progressbar = ttk.Progressbar(root, maximum=100, mode= 'determinate') # 맥시멈 값을 설정, indeterminate는 결정되지않음.
# progressbar.start(10) # 10이면 10ms마다 움직임
# progressbar.pack()


# def btncmd():
#    progressbar.stop() # 작동 중지

# btn = Button(root, text='stop', command=btncmd)
# btn.pack()


p_var2 = DoubleVar() # %는 실수도 가능하도록 더블바를 이용
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
   for i in range(1,101):
      time.sleep(0.01)
      p_var2.set(i)
      progressbar2.update() # 매번 동작할 때마다 GUI를 찍어줌
      if p_var2.get() == 80.0:

         print('80% 입니다')

btn = Button(root, text='start', command=btncmd2)
btn.pack()
root.mainloop()