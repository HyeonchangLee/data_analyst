

# tkinter를 이용한 메모장 프로그램을 만드시오

# [GUI 조건]

# 1. title : 제목없음
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파읾 메뉴 내 열기, 저장, 끝내기 3개만 처리
# 3-1 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2 저장 : mynote.txt 파일에 현재 내용 저장하기
# 3-3 끝내기 : 프로그램 종료
# 4. 프로그램 시작 시 본문은 비어있는 상태
# 5. 하단 status바는 안씀
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정은 가능해야함
# 7. 본문 우측에 상하 스크롤 바 넣기


from tkinter import *
import os


root = Tk() # 시작 시 root를 잡아줌
root.geometry('640x480')
root.title('제목없음')

#frame
frame = Frame(root).pack()

# scrollbar
# scrollbar = Scrollbar(frame).pack(side='right',fill='y')


#fnc
def create_new_file():
    # with open("/Users/hyeonchanglee/Downloads/mynote.txt", "r") as f:
        # f.write(data)
    print('파일 오픈')

def save_file():
    print('파일 저장')
    data = txt.get('1.0',END)
    print(data)

    with open("/Users/hyeonchanglee/Downloads/mynote.txt", "w") as f:
        f.write(data)

   

def end_file():
    print('파일 끝내기')
    root.quit()

# menu
menu = Menu(root)

# 1. 파일
menu_file = Menu(root, tearoff=0)

menu_file.add_command(label='열기', command=create_new_file)
menu_file.add_command(label='저장', command=save_file)
menu_file.add_command(label='끝내기', command=end_file)
menu.add_cascade(label='파일', menu=menu_file)


# 2. 편집
menu_edit = Menu(root, tearoff=0)

menu_edit.add_command(label='편집 하위1')
menu_edit.add_command(label='편집 하위2')
menu.add_cascade(label='편집', menu=menu_edit)


# 3. 서식
menu_format = Menu(root, tearoff=0)

menu_format.add_command(label='서식 하위1')
menu_format.add_command(label='서식 하위2')
menu.add_cascade(label='서식', menu=menu_format)


# 4. 보기
menu_view = Menu(root, tearoff=0)

menu_view.add_command(label='보기 하위1')
menu_view.add_command(label='보기 하위2')
menu.add_cascade(label='보기', menu=menu_view)


# 5. 도움말
menu_help = Menu(root, tearoff=0)

menu_help.add_command(label='도움말 하위1')
menu_help.add_command(label='도움말 하위2')
menu.add_cascade(label='도움말', menu=menu_help)




## 텍스트
# txt = Text(frame, width=640, height=480, yscrollcommand=scrollbar.set).pack(side='left')
txt = Text(frame, width=640, height=480).pack(side='left')




# scrollbar.config(command=txt.yview)
root.config(menu=menu) # 메뉴 설정
root.mainloop() # 끝에 계속 잡아줌
