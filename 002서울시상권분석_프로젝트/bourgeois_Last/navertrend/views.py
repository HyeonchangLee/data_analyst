from django.http import JsonResponse
from django.shortcuts import render
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import urllib.request
from django.views.decorators.csrf import csrf_exempt

pd.options.display.float_format = '{:.2f}'.format

################################네이버 api 불러오는 클래스를 만듬###############################
class NaverDataLabOpenAPI():
    """
    네이버 데이터랩 오픈 API 컨트롤러 클래스
    """

    def __init__(self, client_id, client_secret):
        """
        인증키 설정 및 검색어 그룹 초기화
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.keywordGroups = []
        self.url = "https://openapi.naver.com/v1/datalab/search"

    def add_keyword_groups(self, group_dict):
        """
        검색어 그룹 추가
        """

        keyword_gorup = {
            'groupName': group_dict['groupName'],
            'keywords': group_dict['keywords']
        }
        
        self.keywordGroups.append(keyword_gorup)
        #print(f">>> Num of keywordGroups: {len(self.keywordGroups)}")
        
    def get_data(self, startDate, endDate, timeUnit, device, ages, gender):
        """
        요청 결과 반환
        timeUnit - 'date', 'week', 'month'
        device - None, 'pc', 'mo'
        ages = [], ['1' ~ '11']
        gender = None, 'm', 'f'
        """

        # Request body
        body = json.dumps({
            "startDate": startDate,
            "endDate": endDate,
            "timeUnit": timeUnit,
            "keywordGroups": self.keywordGroups,
            "device": device,
            "ages": ages,
            "gender": gender
        }, ensure_ascii=False)
        
        # Results
        request = urllib.request.Request(self.url)
        request.add_header("X-Naver-Client-Id",self.client_id)
        request.add_header("X-Naver-Client-Secret",self.client_secret)
        request.add_header("Content-Type","application/json")
        response = urllib.request.urlopen(request, data=body.encode("utf-8"))
        rescode = response.getcode()

        if(rescode==200):
            # Json Result
            result = json.loads(response.read()) #결과를 
            
            df = pd.DataFrame(result['results'][0]['data'])[['period']]
            for i in range(len(self.keywordGroups)):
                tmp = pd.DataFrame(result['results'][i]['data'])
                tmp = tmp.rename(columns={'ratio': result['results'][i]['title']})
                df = pd.merge(df, tmp, how='left', on=['period'])
            self.df = df.rename(columns={'period': '날짜'})
            self.df['날짜'] = pd.to_datetime(self.df['날짜'])  
        else:
            print("Error Code:" + rescode)
            
        return self.df

##################################클래스 끝#########################################
##################################광고 API를 불러오기 위한 함수#########################

import hashlib
import hmac
import base64


class Signature:

    @staticmethod
    def generate(timestamp, method, uri, secret_key):
        message = "{}.{}.{}".format(timestamp, method, uri)
        hash = hmac.new(bytes(secret_key, "utf-8"), bytes(message, "utf-8"), hashlib.sha256)

        hash.hexdigest()
        return base64.b64encode(hash.digest())

##################################광고 API를 불러오기 위한 함수 끝########################

# Create your views here.
def search_page(request):
    return render(request, 'search_page.html')


@csrf_exempt
def search_kwd(request):

    area = request.GET['area']   
    keyword_group_set = {
        'keyword_group_1': {'groupName': area+"맛집", 'keywords': [area+"맛집"]}

    }

    # API 인증 정보 설정
    client_id = "ScaTb_f8PQ5GJteI95Kw"
    client_secret = "xMj_ezOoXg"

    # 요청 파라미터 설정
    startDate = "2021-01-01"
    endDate = "2021-12-31"
    timeUnit = 'month'
    device = ''
    ages = []
    gender = ''

    # 데이터 프레임 정의
    naver = NaverDataLabOpenAPI(client_id=client_id, client_secret=client_secret)

    naver.add_keyword_groups(keyword_group_set['keyword_group_1'])

    df = naver.get_data(startDate, endDate, timeUnit, device, ages, gender)

    # 컬럼명을 영어로 바꿔야함
    df.columns = ['date','keyword1']
    df['date'] = ["2021-01",'2021-02','2021-03','2021-04','2021-05','2021-06','2021-07','2021-08','2021-09','2021-10','2021-11','2021-12']

    #null값 0처리
    df = df.fillna(0)

    # 데이터 프레임 -> json으로 보내야함
    body = df.to_json() #컬럼을 기준으로 변환
    body_json = {}
    body_json['json_data'] = json.loads(body) # 한번더 가져와야함


    context = {'body_json':body_json}

    ##########################################################################검색어트렌트 끝 검색광고 시작
    import time
    import random
    import requests

    def get_header(method, uri, api_key, secret_key, customer_id):
        timestamp = str(round(time.time() * 1000))
        signature = Signature.generate(timestamp, method, uri, SECRET_KEY)
        return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': API_KEY, 'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}


    BASE_URL = 'https://api.naver.com'
    API_KEY = '0100000000c63dffc14885e9adfd561cab35084caaf8d4bc9af5b39fe3b5260582fdbd9b8b'
    SECRET_KEY = 'AQAAAADGPf/BSIXprf1WHKs1CEyqpsdNi9REySj221SA7RaxDw=='
    CUSTOMER_ID = '2583176'

    ## 연관키워드
    uri = '/keywordstool'
    method = 'GET'
    #여기서 키워드 수정할 것
    keyword_input = area+'맛집'
    r = requests.get(BASE_URL + uri+'?hintKeywords={}&showDetail=1'.format(keyword_input),headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

    r.json()['keywordList'][0]


    #맛집이라는 검색어가 들어간 것만 출력
    # for i in range(len(r.json()['keywordList'])):
    #     if  '맛집'  in r.json()['keywordList'][i]['relKeyword']:
    #         print(r.json()['keywordList'][i])


    # 출력 예제
    # r.json()['keywordList'][0] 
    # {'relKeyword': '파이썬', #연관 키워드
    #   'monthlyPcQcCnt': 31000, #30일간 pc 조회수
    #   'monthlyMobileQcCnt': 21700, # 30일간 모바일 조회수
    #   'monthlyAvePcClkCnt': 9.1, #4주간 평균 pc 클릭수
    #   'monthlyAveMobileClkCnt': 2.3, # 4주간 평균 모바일 클릭수
    #   'monthlyAvePcCtr': 0.04, #4주간 평균 pc 클릭률
    #   'monthlyAveMobileCtr': 0.02, # 4주간 평균 모바일 클릭률
    #   'plAvgDepth': 8, #4주간 평균 pc 광고수
    #   'compIdx': '중간'} # pc 광고 기반 경쟁력 경쟁정도


    #df로 변경
    import pandas as pd
    df_rk=pd.DataFrame(r.json()['keywordList'])

    # df_rk.rename({'compIdx':'경쟁정도',
    #         'monthlyAveMobileClkCnt':'월평균클릭수_모바일',
    #         'monthlyAveMobileCtr':'월평균클릭률_모바일',
    #         'monthlyAvePcClkCnt':'월평균클릭수_PC',
    #         'monthlyAvePcCtr':'월평균클릭률_PC', 
    #         'monthlyMobileQcCnt':'월간검색수_모바일',
    #         'monthlyPcQcCnt': '월간검색수_PC',
    #         'plAvgDepth':'월평균노출광고수', 
    #         'relKeyword':'연관키워드'},axis=1,inplace=True)
    # print(df_rk.head())


    #컬럼 순서 변경시 예제
    # df=df[['연관키워드', '월간검색수_PC', '월간검색수_모바일',
    #        '월평균클릭수_PC','월평균클릭수_모바일', 
    #        '월평균클릭률_PC','월평균클릭률_모바일',
    #         '경쟁정도','월평균노출광고수']]
    # df.head()

    # 데이터 프레임 -> json으로 보내야함
    body = df_rk.to_json() #컬럼을 기준으로 변환
    ad_json = {}
    ad_json['ad'] = json.loads(body) # 한번더 가져와야함


    #########################네이버 검색광고 api끝#########################



    context = {'body_json':body_json, 'ad_json':ad_json, 'area':area}
    ##################################################
    return JsonResponse(context,safe=False)

