

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By # selenium 새문법

# By.ID  태그 id 값으로 추출
# By.NAME   태그 name 값으로 추출
# By.XPATH  태그 경로로 추출
# By.LINK_TEXT  링크 텍스트 값으로 추출
# By.PARTIAL_LINK_TEXT 링크 텍스트의 자식 텍스트 값 추출
# By.TAG_NAME 태그 이름으로 추출
# By.CLASS_NAME 태그 클래스명으로 추출
# By.CSS_SELECTOR CSS 선택자로 추출

# elem = driver.find_element(By.NAME, "q")
# title = driver.find_element(By.XPATH, r'//*[@id="bestList"]/ol/li[1]/p[1]').text
# driver.find_element(By.XPATH, r'//*[@id="divYes24SCMEvent"]/div[2]/div[2]/a').click()

from bs4 import BeautifulSoup
import requests

import time
import random
from datetime import datetime

import os
import csv
import pandas as pd
import math

key_word = input(str('Type keyword >>> '))

# 파일 저장
# f = open('/Users/hyeonchanglee/Downloads/'+datetime.now().strftime('%Y-%m-%d_%H%M')+'_.csv','w',encoding='utf-8-sig',newline="")
# writer = csv.writer(f)

# title='keyword,product_name,no,customer_id,content,ratings,create_time'
# title=title.split(',')
# writer.writerow(title)


url = 'https://shopping.naver.com/home/p/index.naver' #네이버 쇼핑 진입
options = webdriver.ChromeOptions()
userAgent = "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
options.add_argument(userAgent)
# options.add_argument('headless')
options.add_experimental_option('detach',True)
options.add_argument("no-sandbox")
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR") # 한국어!

browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)

browser.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
browser.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
browser.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })

browser.get(url)

page_html = browser.page_source
soup = BeautifulSoup(page_html,'lxml')

# 네이버 쇼핑 진입 후 검색어 입력 -> 검색
browser.find_element(By.XPATH,'//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div/input').send_keys(key_word) # 키워드 입력
time.sleep(2)
browser.find_element(By.XPATH,'//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div/button[2]').click() # 검색 버튼 클릭돼

# 진입 이후 스크롤 
time.sleep(random.uniform(1,3))
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") #최하단 스크롤
time.sleep(random.uniform(1,3))
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") #최하단 스크롤



# f.close()
# browser.quit()





