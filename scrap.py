# 스크래핑
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


from bs4 import BeautifulSoup
import requests

import time
import random
from datetime import datetime

import os
import csv
import pandas as pd
import math
from selenium.webdriver.common.by import By

import tkinter.messagebox as msgbox

import webbrowser


# 키워드 입력
def input_keyword():
    key_word = entry_keyword.get()
    return key_word

# UserAgent를 크롤링 해 가져오는 함수
def whats_my_UserAgent():
    
    # UserAgent 가져오기
    url_whatismybrowser = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("no-sandbox")
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR") # 한국어!

    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

    browser.get(url_whatismybrowser)

    detected_value = browser.find_element(By.ID, "detected_value")
    userAgent = detected_value.text
    browser.quit()
    return userAgent

# 키워드를 검색하는 함수
def search_data():
    input_keyword() # 입력한 키워드를 받아옴
    msgbox.showinfo('START CRAWLING.....', 'OK버튼을 누르면 시작됩니다. \n 잠시만 기다려주세요.')


    ## 시작
    userAgent = whats_my_UserAgent()
    userAgent = userAgent[:userAgent.index('HeadlessChrome')] # Headless뒷부분을 자름
    url = 'https://www.saramin.co.kr/zf_user/' #사람인
    options = webdriver.ChromeOptions()
    # userAgent = "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    # userAgent = txt_dest_path.get() # 위에서 받아온 userAgent정보를 엔트리에서 가져옴
    options.add_argument(userAgent)
    # options.add_argument('headless')
    # options.add_experimental_option('detach',True)
    options.add_argument("no-sandbox")
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR") # 한국어!

    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

    browser.get(url)

    key_word = input_keyword()
    browser.find_element(By.ID,'search_open').click()
    input = browser.find_element(By.ID,'ipt_keyword_recruit')
    input.send_keys(key_word,Keys.ENTER) # 검색

    browser.find_element(By.XPATH,'//*[@id="recruit_info_list"]/div[2]/div/a').click() # 더보기 클릭

    # 내부 진입
    page_html = browser.page_source
    soup = BeautifulSoup(page_html,'lxml')

    content = soup.find('div',{'class':'content'})
    recruit = content.find_all('div',{'class':'item_recruit'})


    list_box.delete(0,END) # 처음 내부부분 삭제
    for i,r in enumerate(recruit): # 가져온 데이터 출력
            
        # 타이틀
        title = r.find('h2').find('a')['title']

        # 위치, 학력, 경력, 조건
        job_condition = r.find('div',{'class':'job_condition'}).find_all('span')
        if not job_condition:
            job_condition = 'null'

        info =  [x.get_text() for x in job_condition]

        # 회사명
        corp_name = r.find('strong',{'class':'corp_name'}).get_text().strip()

        # url   
        href = r.find('h2').find('a')['href']
        data = title + ' | ' + ','.join(info) + ' | ' + corp_name + ' | ' + 'https://www.saramin.co.kr'+href
        list_box.insert(i,data)

    entry_count.insert(0,i+1) # 개수 세어주는 코드 



# 내부 데이터를 삭제하는 함수
def delete_data():
    list_box.delete('1.0',END) # 처음 내부부분 삭제

# url을 열어주는 함수
import webbrowser
def callback(url): 
    webbrowser.open_new(url)

def go_to_url():
    str_a = list_box.curselection()
    str_b = list_box.get(list_box.curselection())
    # print(str_a)
    print(str_b)
    index = str_b.rfind('|')
    print(str_b[index:])

    callback(str_b[index+2:])





# 1. 레이아웃부터 잡아줌

from tkinter import *
import tkinter.ttk as ttk

root = Tk() # 
root.title('채용 정보 가져오는 프로그램 🧑‍💻') #프로그램 제목 설정
root.geometry('640x480') #가로x세로의 크기를 설정, + 이후로 가로 100, 세로 300으로 위치도 지정 가능


# save address frame
keyword_frame = LabelFrame(root, text='검색어를 입력하세요 🥳')
keyword_frame.pack(fill='x')

entry_keyword = Entry(keyword_frame)
entry_keyword.pack(side='left',fill='x',expand=True, ipady=4) #ipady 높이 변경

btn_data_delete = Button(keyword_frame, text='내용 지우기', width=10, command=delete_data)
btn_data_delete.pack(side='right')

btn_keyword = Button(keyword_frame, text='공고 검색', width=10, command=search_data)
btn_keyword.pack(side='right')

# list frame
list_frame = LabelFrame(root,text='검색 결과입니다 😎')
list_frame.pack(fill='both')

# scroll bar
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right',fill='y')


# list_box = Listbox(root, selectmode='single', height=0) # 하나만 선택, height 는 지정된 숫자의 개수 3이면 3개만 보여짐, 0이면 다보여짐
list_box = Listbox(list_frame, selectmode='single', height=20, yscrollcommand=scrollbar.set) # 여러개 선택 가능
list_box.pack(side='left',fill='both', expand=True)


# 정보 요약 option frame
frame_count = LabelFrame(root, text='정보 요약입니다 🧐')
frame_count.pack()

# 1. 공고 개수 옵션
# 공고 개수 레이블
lbl_count = Label(frame_count, text='공고 개수', width=8)
lbl_count.pack(side='left')

# 공고 개수 엔트리
entry_count = Entry(frame_count, width=5)
entry_count.pack(side='left')

# 2. URL이동 옵션
# URL 이동 레이블
lbl_go_to_url = Label(frame_count, text='선택한 공고 페이지로 이동', width=16)
lbl_go_to_url.pack(side='left')

# URL 이동 버튼
btn = Button(frame_count, text='click', command=go_to_url)
btn.pack(side='left')


# option frame
frame_option = LabelFrame(root, text='세부 옵션 설정입니다 🤧')
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




scrollbar.config(command=list_box.yview)
root.resizable(False, False) # 가로, 세로의 크기를 변경 불가하도록 설정
root.mainloop() # 창이 닫히지 않도록 해줌

