# 1. 레이아웃부터 잡아줌

from tkinter import *
import tkinter.ttk as ttk

root = Tk() # 
root.title('GUI') #프로그램 제목 설정
root.geometry('640x480') #가로x세로의 크기를 설정, + 이후로 가로 100, 세로 300으로 위치도 지정 가능

# file frame (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill='x')

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text = '파일 추가')
btn_add_file.pack(side='left')

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text = '선택 삭제')
btn_del_file.pack(side='right')

# list frame
list_frame = Frame(root)
list_frame.pack(fill='both')

# scroll bar
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right',fill='y')

list_file = Listbox(list_frame, selectmode='extended', height=15, yscrollcommand=scrollbar.set )
list_file.pack(side='left', fill='both',expand=True)

# save address frame
path_frame = LabelFrame(root, text='저장 경로')
path_frame.pack(fill='x')

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side='left',fill='x',expand=True, ipady=4) #ipady 높이 변경

btn_dest_path = Button(path_frame, text='찾아보기', width=10)
btn_dest_path.pack(side='right')

# option frame
frame_option = LabelFrame(root, text='옵션')
frame_option.pack()

# 1. 가로넓이 옵션
# 가로넓이 레이블
lbl_width = Label(frame_option, text='가로넓이', width=8)
lbl_width.pack(side='left')

# 가로넓이 콤보
opt_width = ['원본유지','1024','800','640'] # 콤보박스에 들어갈 값
cmb_width = ttk.Combobox(frame_option, state='readonly', values=opt_width, width=10) #state는 사용자행동 readonly로 수정 불가능 하게 설정
cmb_width.current(0)
cmb_width.pack(side='left')

# 2. 간격옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text='간격', width=8)
lbl_space.pack(side='left')

# 간격 옵션 콤보
opt_space = ['없음','좁게','보통','넓게'] # 콤보박스에 들어갈 값
cmb_space = ttk.Combobox(frame_option, state='readonly', values=opt_space, width=10) #state는 사용자행동 readonly로 수정 불가능 하게 설정
cmb_space.current(0)
cmb_space.pack(side='left')


# 3. 파일 포맷 옵션
# 포맷 옵션 레이블
lbl_format = Label(frame_option, text='포맷', width=8)
lbl_format.pack(side='left')

# 포맷 옵션 콤보
opt_format = ['PNG','JPG','BMP'] # 콤보박스에 들어갈 값
cmb_format = ttk.Combobox(frame_option, state='readonly', values=opt_format, width=10) #state는 사용자행동 readonly로 수정 불가능 하게 설정
cmb_format.current(0)
cmb_format.pack(side='left')




scrollbar.config(command=list_file.yview)
root.resizable(False, False) # 가로, 세로의 크기를 변경 불가하도록 설정
root.mainloop() # 창이 닫히지 않도록 해줌

