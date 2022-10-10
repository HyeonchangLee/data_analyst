

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
 
import os # 파일이 있는지 확인
from tkinter import *

root = Tk() # 시작 시 root를 잡아줌
root.geometry('640x480')
root.title('예딩이의 메모장')

# 열기 저장 파일 이름
filename = 'mynote.txt'

#fnc
def open_file(): # 열기
    if os.path.isfile(filename): #isfile() 파일 이름과 같은 파일이 있는지 확인 
        with open(filename, 'r', encoding='utf-8')as file:
            txt.delete('1.0',END) #    불러오기전에 입력했던 내용 전체 삭제
            txt.insert(END, file.read()) #전체내용 file.read() 을 불러옴//txt.insert(END) 모든내옹을 삽입하는 함수

def save_file(): # 저장
    with open(filename, 'w', encoding='utf-8')as file:
        file.write(txt.get('1.0',END)) #모든 내용을 가져와서 저장

def end_file(): # 끝내기
    print('파일 끝내기')
    root.quit()

# menu
menu = Menu(root)

# 1. 파일
menu_file = Menu(menu, tearoff=0)

menu_file.add_command(label='열기', command=open_file)
menu_file.add_command(label='저장', command=save_file)
menu_file.add_separator()
menu_file.add_command(label='끝내기', command=end_file)
menu.add_cascade(label='파일', menu=menu_file) # 추가 


# 2. 편집
menu_edit = Menu(menu, tearoff=0)

menu_edit.add_command(label='편집 하위1')
menu_edit.add_command(label='편집 하위2')
menu.add_cascade(label='편집', menu=menu_edit)


# 3. 서식
menu_format = Menu(menu, tearoff=0)

menu_format.add_command(label='서식 하위1')
menu_format.add_command(label='서식 하위2')
menu.add_cascade(label='서식', menu=menu_format)


# 4. 보기
menu_view = Menu(menu, tearoff=0)

menu_view.add_command(label='보기 하위1')
menu_view.add_command(label='보기 하위2')
menu.add_cascade(label='보기', menu=menu_view)


# 5. 도움말
menu_help = Menu(menu, tearoff=0)

menu_help.add_command(label='도움말 하위1')
menu_help.add_command(label='도움말 하위2')
menu.add_cascade(label='도움말', menu=menu_help)


# 스크롤바 
# # 다른 위젯이 없으므로 root 바로 집어 넣어도 가능
scrollbar = Scrollbar(root)
scrollbar.pack(side='right',fill='y') # y는 위아래로 늘림 right는 오른쪽에 위치

# 텍스트
# txt = Text(frame, width=640, height=480, yscrollcommand=scrollbar.set).pack(side='left')
txt = Text(root, yscrollcommand=scrollbar.set) # 
txt.pack(side='left',fill='both', expand=True) # expand는 True , fill = both 안해주면 매핑을 못함, 아마 서로 닿아있지 않아서 매핑을못했던것으로 추측

# 설정
scrollbar.config(command=txt.yview) # 텍스트를 매핑
root.config(menu=menu) # 메뉴 설정
root.mainloop() # 끝에 계속 잡아줌
