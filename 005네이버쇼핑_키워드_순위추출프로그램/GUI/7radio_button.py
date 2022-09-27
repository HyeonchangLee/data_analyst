from tkinter import *

## 위젯에 대해서 공부

root = Tk()
root.title('Program1')
root.geometry('640x480')

# radio button은 여러개 중 하나를 선택함
Label(root, text='메뉴를 선택하세요').pack()

burger_var = IntVar() # 인트형으로 값을 저장
btn_burger1 = Radiobutton(root, text='햄버거', value=1, variable=burger_var)  #라디오 버튼이므로 변수를 공유
btn_burger2 = Radiobutton(root, text='치즈버거', value=2, variable=burger_var)  #라디오 버튼이므로 변수를 공유
btn_burger3 = Radiobutton(root, text='치킨버거', value=3, variable=burger_var)  #라디오 버튼이므로 변수를 공유
btn_burger3.select()

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text='음료를 선택하세요').pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text='콜라', value='콜라', variable=drink_var)
btn_drink2 = Radiobutton(root, text='사이다', value='사이다', variable=drink_var)
btn_drink3 = Radiobutton(root, text='환타', value='환타', variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


def btncmd():
   print(burger_var.get()) #선택된 햄버거의 값을 반환 1부터 시작.
   print(drink_var.get()) #선택된 햄버거의 값을 반환 1부터 시작. 사이라 라고 반환됨


btn = Button(root, text='click', command=btncmd)
btn.pack()

root.mainloop()