from tkinter import *
import tkinter.messagebox as msgbox

## 위젯에 대해서 공부

root = Tk()
root.title('Program1')
root.geometry('640x480')

# 기차 예매 시스템이라고 가정
def info():
   msgbox.showinfo('알림', '정상적으로 예매 완료되었습니다.')

def warn():
   msgbox.showwarning('경고', '해당좌석은 매진되었습니다.')

def error():
   msgbox.showerror('에러', '결제 오류가 발생하였습니다.')

def okcancel():
   msgbox.askokcancel('확인 / 취소', '해당 좌석을 예매하시겠습니까?')

def retrycancel():
   msgbox.askretrycancel('재시도 / 취소', '일시 오류입니다. 다시 시도하시겠습니까?')

def yesno():
   msgbox.askyesno('예 / 아니오', '역방향입니다, 예매하시겠습니까?')

def yesnocancel():
   response = msgbox.askyesnocancel(title=None, message='예매 내역이 저장되지 않았습니다. 저장 후 프로그램을 종료하시겠습니까?')
   # 네 : 저장 후 종료
   # 아니오 : 저장 하지않고 종료
   # 취소 : 프로그램 종료 취소
   
   print('응답 : ',response)
   if response == 1: # True는 1로 출력돰
      print('yes')
   elif response == 0: # False는 0으로 출력됨
      print('no')
   else:
      print('cancel')   

Button(root, command=info, text='알림').pack()
Button(root, command=warn, text='경고').pack()
Button(root, command=error, text='에러').pack()

Button(root, command=okcancel, text='확인 취소').pack()
Button(root, command=retrycancel, text='재시도 취소').pack()
Button(root, command=yesno, text='예 아니오').pack()
Button(root, command=yesno, text='예 아니오').pack()
Button(root, command=yesnocancel, text='예 아니오 취소').pack()

root.mainloop()