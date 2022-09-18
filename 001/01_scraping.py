# 유튜브의 댓글을 크롤링

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

# 파일 저장 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# f = open('/Users/hyeonchanglee/Documents/data_analyst/001/'+datetime.now().strftime('%Y-%m-%d_%H%M')+'re.csv','w',encoding='utf-8-sig',newline="")
# writer = csv.writer(f)

# title='product_name,no,customer_id,content,ratings,create_time'
# title=title.split(',')
# writer.writerow(title)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# 애플 브랜드관의 1페이지부터 3페이지까지 댓글데이터를 가져옴

url = 'https://www.youtube.com/c/%EC%9A%B0%EC%A0%95%EC%9E%89%ED%8A%9C%EB%B8%8C' #유튜브
options = webdriver.ChromeOptions()
userAgent = "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
options.add_argument(userAgent)
# options.add_argument('headless')
options.add_experimental_option('detach',True)
options.add_argument("no-sandbox")
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR") # 한국어!

browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
browser.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
browser.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
browser.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })

browser.get(url)

page_html = browser.page_source
soup = BeautifulSoup(page_html,'lxml')

videos = browser.find_element_by_xpath('//*[@id="tabsContent"]/tp-yt-paper-tab[2]').click() #상품 리뷰 클릭




# productList = soup.find('ul',{'id':'productList'}) # 애플 제품들의 전체 리스트
# items = productList.find_all('li',{'class':'baby-product'}) # 리스트의 내부 섹션

# # 애플 제품들에 하나씩 접근
# for i,item in enumerate(items):
#     # if i==20:
#     #     break
#     main_url = 'https://www.coupang.com'
#     url = main_url+item.find('a')['href']
#     time.sleep(random.uniform(4,6))
#     browser.get(url)


#     time.sleep(random.uniform(4,6))
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") #최하단 스크롤
#     time.sleep(2)
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") #최하단 스크롤
#     browser.find_element_by_xpath('//*[@id="btfTab"]/ul[1]/li[2]').click() #상품 리뷰 클릭
    
#     time.sleep(random.uniform(4,6))
#     page_html  = browser.page_source
#     elem = BeautifulSoup(page_html,'lxml')
#     review_count = int(elem.find('div',{'class',"sdp-review__average__total-star__info-count"}).get_text().replace(',','')) #리뷰 수 출력
#     print('review_count : ',review_count) # 리뷰가 전체 몇개인지 확인



#     # 페이지의 소스 정보를 확인 후 리뷰 섹션으로 이동해서 리뷰 5개를 가져오고 이후 다음 페이지를 눌러 다음 5개의 리뷰를 가져오는 함수를 생성
#     def digger():
#         # 페이지 정보 가져오기
#         page_html  = browser.page_source
#         elem = BeautifulSoup(page_html,'lxml')
        
#         # 페이지 내의 리뷰 섹션으로 이동
#         p_name = elem.find('h2',{'class':'prod-buy-header__title'}).get_text() #상품명 출력
#         print('#'*40+str(i+1)+p_name+'#'*40) # 어떤 상품으로 들어왔는지 확인
#         boxes = elem.find_all('article',{'class':'sdp-review__article__list'}) # 리뷰가 있는 부분
        
#         # 5개의 리뷰를 하나씩 출력
#         for j,box in enumerate(boxes):
#             data = []

#             #j는 한 아이템의 리뷰 번호
#             name = box.find('span',{'class':'sdp-review__article__list__info__user__name'}).get_text().strip() # 유저 이름이 기록
#             ratings = box.find('div',{'class':'sdp-review__article__list__info__product-info__star-orange'})['data-rating'].strip() #평점 기록
#             create_date = box.find('div',{'class':'sdp-review__article__list__info__product-info__reg-date'}).get_text().strip() #날짜가 기록
#             review_content = box.find('div',{'class':'sdp-review__article__list__review__content'})
#             if not review_content:
#                 head_line = box.find('div',{'class':'sdp-review__article__list__headline'}) # 헤드라인 내용
#                 if not head_line:
#                     # review_content = '0' #내용이 없는 경우 이므로 더미값 입력
#                     continue # 없을경우 그냥 스킵.
#                 else:
#                     review_content = box.find('div',{'class':'sdp-review__article__list__headline'}).get_text().strip() #없을 경우 헤드라인으로
#             else:
#                 review_content = box.find('div',{'class':'sdp-review__article__list__review__content'}).get_text().strip() #내부 댓글을 확인 (있는 경우 그냥)
                

#             # p_name 상품명
#             print('*이름 : ',name,'******')
#             print('*평점 : ',ratings,'******')
#             print('*생성일시 : ',create_date,'******')
#             print('*내용 : ',review_content,'******')

#             # 리뷰를 파일로 저장
#             data.append(p_name)
#             data.append(j+1)
#             data.append(name)
#             data.append(review_content)
#             data.append(ratings)
#             data.append(create_date)
#             writer.writerow(data)
#     #digger끝

#     browser.find_element_by_xpath('//*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[2]/div[3]').click() #전체 클릭
#     time.sleep(2)

#     # //*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[2]/div[3]/div[2]/ul/li[1] #최고
#     # //*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[2]/div[3]/div[2]/ul/li[2]
#     # //*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[2]/div[3]/div[2]/ul/li[5] #최악
    
#     try:
#         # for p2 in range(1,2): #평점 1부터 평점 5까지
#         p2 = 1

#         browser.find_element_by_xpath('//*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[2]/div[3]').click() #전체 클릭
#         time.sleep(2)

#         browser.find_element_by_xpath('//*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[2]/div[3]/div[2]/ul/li['+str(p2)+']').click() #별로 클릭
#         time.sleep(2)

#         review_count = int(elem.find('div',{'class':'sdp-review__article__order__star__all__current__count js_reviewArticleCurrentStarCount5'}).get_text().replace(',','')) #리뷰 수 출력
#         for page in range((review_count//5)//10):
#             print('page : ',page)
#             for p in range(3,12): # 2페이지부터 10페이지 까지
#                 time.sleep(2)
#                 digger() # 1페이지 출력

#                 # 2페이지 ~10페이지
#                 browser.find_element_by_xpath('//*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[4]/div[3]/button['+str(p)+']').click()
#                 time.sleep(2)
#                 print('page',str(p))
#                 digger() 

#             # 10페이지 지나면 다음 페이지 클릭
#             time.sleep(2)
#             browser.find_element_by_xpath('//*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[4]/div[3]/button[12]').click()
#     except:
#         pass



# f.close()
# browser.quit()




