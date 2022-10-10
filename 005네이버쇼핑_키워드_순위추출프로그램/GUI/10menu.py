from tkinter import *


## 위젯에 대해서 공부

root = Tk()
root.title('Program1')
root.geometry('640x480')

def create_new_file():
   print('새 파일을 만듭니다.')

menu = Menu(root) # 메뉴 정의

# 파일 메뉴
menu_file = Menu(menu, tearoff=0) # 

menu_file.add_command(label='New File', command=create_new_file) # 첫번째 항목
menu_file.add_command(label='New Window') # 두번째
menu_file.add_separator() # 구분자
menu_file.add_command(label='Open File...') # 마지막
menu_file.add_separator() # 구분자
menu_file.add_command(label='Save All', state='disable')
menu_file.add_separator() # 구분자
menu_file.add_command(label='Exit',command=root.quit) # 파일 종료

menu.add_cascade(label='File',menu=menu_file) # 전체 큰 메뉴바에 file이라는 레이블로 menu_file을 설정한 항목을 출력
# 에딧 메뉴

menu.add_cascade(label='Edit') # 빈값

# Language메뉴 추가(radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label='Python')
menu_lang.add_radiobutton(label='JAVA')
menu_lang.add_radiobutton(label='C++')
menu.add_cascade(label='Language', menu=menu_lang)

# view 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label='Show Minimap')
menu.add_cascade(label='View', menu=menu_view)



root.config(menu=menu)

root.mainloop()