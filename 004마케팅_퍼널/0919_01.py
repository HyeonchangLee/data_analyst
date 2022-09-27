# https://www.kaggle.com/datasets/olistbr/marketing-funnel-olist
# https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce


# 이커머스 전체의 데이터셋이 있고 이를 어떻게 가공하여 분석할 것인지 가이드를 확인


# 데이터 집합 정보
# 올리스트별 마케팅 퍼널  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 어서오세요! 이것은 올리스트 스토어에서 제품을 판매하기 위해 연락 요청을 작성한 셀러들의 마케팅 퍼널 데이터 세트입니다. 
# 데이터 세트에는 2017년 6월 1일부터 2018년 6월 1일까지 연락을 요청한 8k Marketing Qualified Leads(MQLs)의 정보가 있습니다. 
# 이들은 MQL의 총합에서 랜덤하게 표본 추출되었습니다.
# 이 기능은 영업 프로세스를 리드 범주, 카탈로그 크기, 행동 프로파일 등 다양한 차원에서 볼 수 있도록 지원합니다.
# 이것은 실제 데이터이며, 원래 데이터 세트에서 익명화되고 샘플링되었습니다.

# Olist의 브라질 E-Commerce 공용 데이터 세트 개요 - - - - - - - - - - - - - - - - - - - - - - - -
# 이 데이터 세트는 seller_id를 사용하여 Olist의 브라질 E-Commerce Public Dataset에 연결할 수도 있습니다.
# 100,000개의 주문, 가격, 결제, 화물 성능, 고객 위치, 제품 속성 및 고객이 작성한 최종 리뷰 정보를 볼 수 있습니다.

# 문맥 
# 이 데이터 세트는 브라질 시장에서 가장 큰 백화점인 Olist가 제공했다. 
# Olist는 브라질 전역에서 온 소규모 기업들을 번거로움 없이 하나의 계약으로 채널에 연결한다.
# 이러한 상인들은 올리스트 스토어를 통해 제품을 판매하고 올리스트 물류 파트너를 사용하여 고객에게 직접 배송할 수 있습니다. 
# 웹사이트 www.olist.com에서 더 많은 정보를 볼 수 있다.

# 셀러는 이 데이터 세트에서 공개된 마케팅 및 판매 퍼널를 통해 올리스트에 가입합니다. 
# 단계 설명:

# 1. 랜딩 페이지에서 가입합니다.
# 2. SDR(Sales Development Representation)의 연락을 받고 몇 가지 정보를 확인하고 컨설팅을 예약합니다.
# 3. 컨설팅은 영업 담당자(SR)가 담당합니다. SR이 거래를 성사시키거나(리드 싱업) 거래에서 실패할 수 있음(가입하지 않고 이탈)
# 4. 리드는 판매자가 되어 올리스트에 자신의 카탈로그를 만들기 시작한다.
# 5. 그의 제품들은 시장에 출시되었고 팔 준비가 되었습니다!


# 주의
# 셀러 MQL은 여러 소스에서 나올 수 있습니다(예를 들어, 두 개의 다른 랜딩 페이지에 구독할 수 있음).
# 랜딩 페이지 예제
# 랜딩 페이지 예제


# 데이터 스키마
# 데이터는 더 나은 이해와 구성을 위해 여러 데이터 세트로 나뉜다. 작업 시 다음 데이터 스키마를 참조하십시오.


# 영감
# 다음은 이 데이터 집합에서 가능한 결과에 대한 몇 가지 영감을 제공합니다.

# 고객 수명 가치(LTV): 
# 고객이 향후 수익을 얼마나 올릴 것인가?

# SR/SDR 최적화:
# 어떤 SR 또는 SDR이 각 유형의 리드와 대화해야 합니까?

# 마감 예측(Closing Prediction):
# 어떤 거래가 성사됩니까?

# EDA:


# 데이터 셋 설명 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('/Users/hyeonchanglee/Documents/data_analyst/004마케팅_퍼널/Marketing_Funnel_by_Olist/olist_marketing_qualified_leads_dataset.csv')
# print(df)

# df2 = pd.read_csv('/Users/hyeonchanglee/Documents/data_analyst/004마케팅_퍼널/Marketing_Funnel_by_Olist/olist_closed_deals_dataset.csv')
# print(df2.iloc[0])
# print(df2.iloc[1])



crm_dataset = pd.read_csv('/Users/hyeonchanglee/Documents/data_analyst/004마케팅_퍼널/CRM_dataset/CRM_dataset.csv', encoding = 'unicode_escape')

print(crm_dataset)
print(crm_dataset.info())



# to_mysql 

