
# CRM 분석이란 무엇인가?

# CRM 분석은 귀사의 판매 및 고객 서비스 성과를 입증하는 데이터입니다. 또한 CRM 분석은 보다 현명한 비즈니스 의사 결정을 알리는 데 사용할 수 있는 고객 데이터를 제공합니다. 일반적으로 CRM 소프트웨어를 사용하여 CRM 분석을 얻고 모든 데이터 수집 및 보고서 생성을 자동화합니다.

# CRM 분석의 이점

# CRM 분석의 주요 이점은 이를 사용하여 영업, 고객 서비스 및 마케팅 프로세스를 알릴 수 있다는 것입니다. CRM 분석을 사용하여 다음을 통해 방법을 개선할 수 있습니다.

# 고객 서비스 평가. CRM 분석은 고객 서비스 팀의 성과를 알려줍니다. 팀이 개선할 수 있는 수치를 발견하면, 이러한 목표를 향해 팀을 추진하는 관행을 구현하십시오.
# 정확한 고객 데이터. 고객 데이터를 인구 통계 마케팅 또는 전자 메일 마케팅에 사용하든, 적합한 사람에게 연락하고 있는지 알아야 합니다. CRM 분석은 당신이 그것을 하고 있다는 것을 보장한다.
# 철저한 고객 분석. 당신의 고객은 보통 한 분기당 얼마를 소비합니까? 같은 제품을 몇 번이고 사는 건가요, 아니면 다른 건가요? CRM 분석을 통해 이러한 질문에 대한 확실한 답을 얻을 수 있으며, 배운 내용을 사용하여 마케팅 전략을 개선할 수 있습니다.
# 효율적인 리드 생성. 당신의 CRM 분석은 당신의 마케팅 노력 중 어떤 것이 구매와 가장 강하게 관련이 있는지 알려줄 수 있다. 구매와 밀접한 관련이 있는 한 가지 접근 방식이 있지만 이러한 접근 방식을 통해 일부 고객만을 대상으로 했다면, 이 방법을 더 시도해 보십시오. 즉, 매출이 증가할 수 있습니다.
# 데이터 셋 설명 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# !pip install plotly
# !pip install Lifetimes

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기 : 
crm_dataset = pd.read_csv('/Users/hyeonchanglee/Documents/data_analyst/004마케팅_퍼널/CRM_dataset/CRM_dataset.csv', \
    encoding = 'unicode_escape',dtype = {'CustomerID': str,'InvoiceID': str},)

# 문자에서 날짜형으로 변경
crm_dataset['InvoiceDate'] = pd.to_datetime(crm_dataset['InvoiceDate'])
# crm_dataset['InvoiceNo'].astype(str)
# crm_dataset['CustomerID'].astype(str)

df = crm_dataset.copy()

#1. Libraries and Utilities, Load and Check Data, Understanding Data

# 일반적으로 전자 상거래 데이터 세트는 독점적이며 결과적으로 공개적으로 사용 가능한 데이터 중에서 찾기 어렵다. 
# 그러나 UCI 기계 학습 저장소는 2010년과 2011년의 실제 트랜잭션을 포함하는 이 데이터 세트를 만들었다. 
# 데이터 세트는 "온라인 소매"라는 제목으로 찾을 수 있는 사이트에서 유지된다.

# 📃 변수 설명

# 송장번호 : 6자리로 구성된 송장번호입니다. 이 코드가 문자 'c'로 시작하면 취소를 나타냅니다.
# 재고코드 : 5자리로 구성된 상품코드입니다.
# 설명: 상품명.
# 수량: 트랜잭션당 각 제품의 수량입니다.
# 송장 날짜: 각 트랜잭션이 생성된 날짜와 시간을 나타냅니다.
# 단가: 개당 제품 가격.
# 고객.ID : 5자리 고객번호입니다. 고객마다 고유한 고객 ID가 있습니다.
# 국가: 각 고객이 거주하는 국가 이름

# # <1. 데이터 셋 확인>
# print(df.head()) # 상위 5
# print('- - '*50)
# print(df.tail()) # 하위 5
# print('- - '*50)
# print('null의 개수 :\n',df.isna().sum()) # null 확인
# print('- - '*50)
# print('중복 된 개수 :',df.duplicated().sum()) # 중복값 확인

# <2. 세계 지도로 분포 확인>
# 고객아이디, 송장번호, 국가순으로 그룹, reset_index를 통해 인덱스를 없앰
world_map = df[['CustomerID','InvoiceNo','Country']].groupby(['CustomerID','InvoiceNo','Country']).count().reset_index(drop=False)
countries = world_map['Country'].value_counts() # 국가 컬럼의 값 개수를 셈
# print(world_map)
# print(contries)

data = dict(type='choropleth',
            locations = countries.index,
            locationmode = 'country names',
            z = countries,
            text = countries.index,
            colorbar = {'title':'Orders'},
            colorscale='Viridis',
            reversescale = False)

layout = dict(title={'text': "Number of Orders by Countries",
                     'y':0.9,
                     'x':0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
              geo = dict(resolution = 50,
                         showocean = True,
                         oceancolor = "LightBlue",
                         showland = True,
                         landcolor = "whitesmoke",
                         showframe = True),
             template = 'plotly_white',
             height = 600,
             width = 1000)

choromap = go.Figure(data = [data], layout = layout)
iplot(choromap, validate = False)