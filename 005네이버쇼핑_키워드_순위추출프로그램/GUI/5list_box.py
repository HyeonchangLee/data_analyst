from tkinter import *

## 위젯에 대해서 공부

root = Tk()
root.title('Program1')
root.geometry('640x480')

# list_box = Listbox(root, selectmode='single', height=0) # 하나만 선택, height 는 지정된 숫자의 개수 3이면 3개만 보여짐, 0이면 다보여짐
list_box = Listbox(root, selectmode='extended', height=0) # 여러개 선택 가능
list_box.insert(0,'사과')
list_box.insert(1,'딸기')
list_box.insert(2,'바나나')
list_box.insert(END,'수박')
list_box.insert(END,'포도')
list_box.pack()

def btncmd():
    # list_box.delete(END) # 맨뒤의 아이템을 클릭시 삭제
    # list_box.delete(0) # 맨앞의 아이템을 클릭시 삭제
    
    # 개수 확인
    # print('리스트에는',list_box.size(),'개가 있어요')

    # 항목 확인
    # print('1번째부터 3번째 항목 : ',list_box.get(0,2)) #0~2의 인덱스 아이템을 가져옴 1번째부터 3번째 항목 :  ('사과', '딸기', '바나나')
    
    # 선택된 항목 확인
    print('선택된 항목 : ',list_box.curselection()) # 현재 선택된 항목의 인덱스를 가져옴 선택된 항목 :  (0, 1, 2, 4)




btn = Button(root, text='click', command=btncmd)
btn.pack()

root.mainloop()