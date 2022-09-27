from time import strftime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

df = pd.read_excel('/Users/hyeonchanglee/Documents/data_analyst/004마케팅_퍼널/cohort_dataset01/cohort_test.xlsx')

# print(df.head())

# orderperiod 라는 컬럼을 새로 만들어 YYYY-MM 형식으로 월별 데이터를 뽑아냄

# 컬럼명 소문자로 변경
df.columns = ['order_id','order_date','user_id','total_charges','common_id','pup_id','pickup_date']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# <1> YYYY-MM 형의 데이터를 가진 컬럼을 생성 : 월별 코호트 실행을 위해?
df['order_period'] = df['order_date'].apply(lambda x : x.strftime('%Y-%m'))

# print(df.groupby('user_id').min()) # user_id 컬럼을 기준으로 그룹화 (유저 아이디로 묶음)

# df['cohort_period'] =  df[['user_id','order_date']].groupby('user_id')['order_date'].min().apply(lambda x : x.strftime('%Y-%m'))
# print(df)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# <2> 코호트 월을 생성합니다
# 인덱스를 유저 아이디로 설정 이후 -> 첫 구매월을 추출해서 새 컬럼을 생성 -> 인덱스를 해제
df.set_index('user_id',inplace=True)
df['cohort_group'] = df.groupby(level=0)['order_date'].min().apply(lambda x : x.strftime('%Y-%m')) # 유저 아이디로 그룹화해 min을 통해 처음 주문일자를 찾아서 적용
df.reset_index(inplace=True)
# print(df.head(20))

# 유저 아이디 47이 가장 먼저 구매한 달은 2009-01 이므로 코호트 기간을 2009-01


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# <3> 코호트를 쪼갬

grouped = df.groupby(['cohort_group','order_period']) # cohort로 먼저 정렬 이후 order_period로 정렬
print(grouped)

# agg 다양한 함수를 한번에 적용
cohorts = grouped.agg({'user_id': pd.Series.nunique, # 유저 아이디의 유니크 개수를 셈으로 써 유저 수를 추출
                        'order_id': pd.Series.nunique, # 오더 아이디의 유니크 개수를 셈으로 써 유저 수를 추출
                        'total_charges': np.sum }) # 금액을 더함으로써 월별 코호트별 구매 금액을 추출

cohorts.rename(columns={'user_id': 'total_users', 'order_id' : 'total_orders'}, inplace=True)
print(cohorts.loc['2009-01']) #2009-01 월 코호트

# results
#   total_users  total_orders  total_charges
# order_period                                          
# 2009-01                22            30      1850.2550
# 2009-02                 8            25      1351.0650
# 2009-03                10            26      1357.3600
# 2009-04                 9            28      1604.5000
# 2009-05                10            26      1575.6250
# 2009-06                 8            26      1384.8400
# 2009-07                 8            24      1750.8400
# 2009-08                 7            21      1426.5714
# 2009-09                 7            24      1964.2755
# 2009-10                 7            13       860.3292
# 2009-11                 7            21      1821.8153
# 2009-12                 8            22      2152.1165
# 2010-01                11            25      2084.2236
# 2010-02                 7            19      2068.7771
# 2010-03                 6            12      1504.3325
# 첫 구매가 2009-01인 고객이 이후에 얼마나 구매하는지 확인할 수 있다.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# <4> cohort 기간 컬럼을 생성
# cohort_period를 구하는 함수
def cohort_period(df):
    df['cohort_period'] = np.arange(len(df)) +1 # np.arange(시작점(생략 시 0), 끝점(미포함), step size(생략 시 1)) 인자
    return df

# print(cohorts)
# gropupby로 묶으면 별개의 데이터 프레임으로 인식하므로 이런식으로 

#                            total_users  total_orders  total_charges  cohort_period
# cohort_group order_period                                                         
# 2009-01      2009-01                22            30      1850.2550              1
#              2009-02                 8            25      1351.0650              2
#              2009-03                10            26      1357.3600              3
#              2009-04                 9            28      1604.5000              4
#              2009-05                10            26      1575.6250              5
#              2009-06                 8            26      1384.8400              6
#              2009-07                 8            24      1750.8400              7
#              2009-08                 7            21      1426.5714              8
#              2009-09                 7            24      1964.2755              9
#              2009-10                 7            13       860.3292             10
#              2009-11                 7            21      1821.8153             11
#              2009-12                 8            22      2152.1165             12
#              2010-01                11            25      2084.2236             13
#              2010-02                 7            19      2068.7771             14
#              2010-03                 6            12      1504.3325             15
# 2009-02      2009-02                15            15       666.3100              1
#              2009-03                 3             8       501.6100              2
#              2009-04                 5            10       968.7800              3

cohorts = cohorts.groupby(level=0).apply(cohort_period)
print(cohorts.head(20))

# CohortGroup를 기준으로 Group화를 한 후 CohortPeriod 컬럼을 생성한 후 OrderPeriod와의 순서를 정합니다. 하기 그림의 위치를 정하기 위함입니다.  np.arrange()의 사용법을 알면 도움이 됩니다.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# <5> 기입된 자료가 올바른지 확인

x = df[(df.cohort_group == '2009-01') & (df.order_period == '2009-01')]
y = cohorts.loc[('2009-01', '2009-01')]

assert(x['user_id'].nunique() == y['total_users'])
assert(x['total_charges'].sum().round(2) == y['total_charges'].round(2))
assert(x['order_id'].nunique() == y['total_orders'])

x = df[(df.cohort_group == '2009-01') & (df.order_period == '2009-09')]
y = cohorts.loc[('2009-01', '2009-09')]

assert(x['user_id'].nunique() == y['total_users'])
assert(x['total_charges'].sum().round(2) == y['total_charges'].round(2))
assert(x['order_id'].nunique() == y['total_orders'])

x = df[(df.cohort_group == '2009-05') & (df.order_period == '2009-09')]
y = cohorts.loc[('2009-05', '2009-09')]

assert(x['user_id'].nunique() == y['total_users'])
assert(x['total_charges'].sum().round(2) == y['total_charges'].round(2))
assert(x['order_id'].nunique() == y['total_orders'])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# <6> 코호트의 베이스 값 가져옴

cohorts.reset_index(inplace=True)
cohorts.set_index(['cohort_group','cohort_period'], inplace=True)

cohort_group_size = cohorts['total_users'].groupby(level=0).first() # first는 그룹내에 첫번째 값을 가져옴
# 각 Cohort그룹별 Base를 가져오기 위해 CohortGroup별로 전체 고객 수의 첫 번째 값을 가져오기 위해 first()를 지정한다. 

print(cohort_group_size)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# <7> 월별 잔존율 도출

print('-'*60 + 'HEAD' +'-'*60 )
print(cohorts.head())

print('-'*60 + 'UNSTACK' +'-'*60 )
print(cohorts['total_users'].unstack(0)) # unstack 데이터의 구조를 왼쪽에서 오른쪽으로 변경 0 인덱스 기준
print(cohorts['total_users'])

# 원래 구조
# cohort_group  cohort_period
# 2009-01       1                 22
#               2                  8
#               3                 10
#               4                  9
#               5                 10
#                               ... 
# 2010-01       2                 50
#               3                 26
# 2010-02       1                100
#               2                 19
# 2010-03       1                 24

# unstack된 구조
# cohort_group   2009-01  2009-02  2009-03  2009-04  2009-05  2009-06  ...  2009-10  2009-11  2009-12  2010-01  2010-02  2010-03
# cohort_period                                                        ...                                                      
# 1                 22.0     15.0     13.0     39.0     50.0     32.0  ...     54.0    130.0     65.0     95.0    100.0     24.0
# 2                  8.0      3.0      4.0     13.0     13.0     15.0  ...     17.0     32.0     17.0     50.0     19.0      NaN
# 3                 10.0      5.0      5.0     10.0     12.0      9.0  ...     12.0     26.0     18.0     26.0      NaN      NaN
# 4                  9.0      1.0      4.0     13.0      5.0      6.0  ...     13.0     29.0      7.0      NaN      NaN      NaN
# 5                 10.0      4.0      1.0      6.0      4.0      7.0  ...     13.0     13.0      NaN      NaN      NaN      NaN
# 6                  8.0      4.0      2.0      7.0      6.0      5.0  ...      7.0      NaN      NaN      NaN      NaN      NaN
# 7                  8.0      4.0      2.0      4.0      3.0      3.0  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 8                  7.0      5.0      3.0      6.0      5.0      3.0  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 9                  7.0      5.0      2.0      2.0      5.0     10.0  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 10                 7.0      4.0      1.0      4.0      4.0      3.0  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 11                 7.0      3.0      3.0      3.0      3.0      NaN  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 12                 8.0      3.0      2.0      2.0      NaN      NaN  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 13                11.0      5.0      1.0      NaN      NaN      NaN  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 14                 7.0      NaN      NaN      NaN      NaN      NaN  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 15                 6.0      NaN      NaN      NaN      NaN      NaN  ...      NaN      NaN      NaN      NaN      NaN      NaN

print('-'*60 + 'DEVIDE' +'-'*60 )
print(cohorts['total_users'].unstack(0).divide(cohort_group_size,axis=1).round(2))

# ------------------------------------------------------------DEVIDE------------------------------------------------------------
# cohort_group   2009-01  2009-02  2009-03  2009-04  2009-05  2009-06  ...  2009-10  2009-11  2009-12  2010-01  2010-02  2010-03
# cohort_period                                                        ...                                                      
# 1                 1.00     1.00     1.00     1.00     1.00     1.00  ...     1.00     1.00     1.00     1.00     1.00      1.0
# 2                 0.36     0.20     0.31     0.33     0.26     0.47  ...     0.31     0.25     0.26     0.53     0.19      NaN
# 3                 0.45     0.33     0.38     0.26     0.24     0.28  ...     0.22     0.20     0.28     0.27      NaN      NaN
# 4                 0.41     0.07     0.31     0.33     0.10     0.19  ...     0.24     0.22     0.11      NaN      NaN      NaN
# 5                 0.45     0.27     0.08     0.15     0.08     0.22  ...     0.24     0.10      NaN      NaN      NaN      NaN
# 6                 0.36     0.27     0.15     0.18     0.12     0.16  ...     0.13      NaN      NaN      NaN      NaN      NaN
# 7                 0.36     0.27     0.15     0.10     0.06     0.09  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 8                 0.32     0.33     0.23     0.15     0.10     0.09  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 9                 0.32     0.33     0.15     0.05     0.10     0.31  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 10                0.32     0.27     0.08     0.10     0.08     0.09  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 11                0.32     0.20     0.23     0.08     0.06      NaN  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 12                0.36     0.20     0.15     0.05      NaN      NaN  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 13                0.50     0.33     0.08      NaN      NaN      NaN  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 14                0.32      NaN      NaN      NaN      NaN      NaN  ...      NaN      NaN      NaN      NaN      NaN      NaN
# 15                0.27      NaN      NaN      NaN      NaN      NaN  ...      NaN      NaN      NaN      NaN      NaN      NaN



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# <8> 월별 잔존율 도출

user_retention = cohorts['total_users'].unstack(0).divide(cohort_group_size,axis=1)
user_retention[['2009-06','2009-07','2009-08']].plot(figsize=(10,5))
plt.title('Cohorts : User Retention')
plt.xticks(np.arange(1,12.1,1))
plt.xlim(1,12)
plt.ylabel('% of Cohort Purcharsing')
plt.show()

import seaborn as sns
sns.set(style='white')

plt.figure(figsize=(10,5))
plt.title('Cohorts: User Retention')
sns.heatmap(user_retention.T,annot=True,fmt='.0%')
plt.show()