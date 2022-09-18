import pandas as pd
import numpy as np

# ##데이터 전처리 - 전처리코드에서 점포부분 가져옴##
df=pd.read_excel('/Users/hyeonchanglee/Documents/pydata/10.project/0610/bourgeois0610/zprojectdata/점포_z.xlsx')
# print(df.columns)

# Index(['기준_년_코드', '기준_분기_코드', '상권_코드', '상권_코드_명', '서비스_업종_코드', '점포_수',
#        '유사_업종_점포_수', '프랜차이즈_점포_수'],
#       dtype='object')


# # print(df)
# year=[2019,2020,2021]
# bungi=[1,2,3,4]

# sg=df['상권_코드'].unique() 
# y=['CS100001','CS100002','CS100003','CS100004','CS100005','CS100006','CS100007','CS100008','CS100009','CS100010']
# z=[]
# for aa in year:
#     for bb in bungi:
#         a=df[(df['기준_년_코드']==aa) & (df['기준_분기_코드']==bb)]
#         for i in sg:
#             for j in y:

#                 x_1=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'점포_수'}])
#                 x_2=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'유사_업종_점포_수'}])
#                 x_3=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'프랜차이즈_점포_수'}])
#                 h=[aa,bb,i,j,x_1,x_2,x_3]



#                 z.append(h)
# aaa=pd.DataFrame(z,columns=['년도','분기','지역','서비스_업종_코드','점포','유사','프렌차이즈'])


# #raw data
# # print(aaa)

# print(aaa[''])


#14:10시작 데이터 삽입 -> 

#########################################################################################
#matplotlib으로 시각화해서 내용 확인


# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.rcParams['font.family'] ='Malgun Gothic'
# matplotlib.rcParams['font.size'] = 15
# matplotlib.rcParams['axes.unicode_minus'] = False
# import pandas as pd
# import numpy as np

# # p1 = p1.head(10).sort_values( by='전체', ascending=False)

# x = p1['지역'] 
# y = p1['전체'] 
# y2 = p1['식료품']

# arrx = np.array(x)
# arry = np.array(y,dtype=float)
# arry2 = np.array(y2,dtype=float)

# percent1 = arry2/arry
# print(percent1)

# percent1 = np.round(percent1,2)

# plt.bar(x,y)

# for i,txt in enumerate(y):
    
#     plt.text(x[i],y[i],txt,ha='center')
    
# plt.bar(x,y2)

# for i,txt in enumerate(y2):
#     plt.text(x[i],y2[i],percent1[i],ha='center')
    
# # y축 그래프의 범위를 제한
# # plt.ylim(160,220)
# plt.show()


# #########################################################################################
# # #오라클db에 분석한 데이터 삽입############################################################
# # import cx_Oracle

# #SQL로 테이블 생성
# # create table project_category_analytics (
# #     loc varchar2(20) primary key,
# #     expenditure_all  varchar2(20),
# #     expenditure_food  varchar2(20)
# # );

# x = list(p1['지역'] )
# y = list(p1['전체'] )
# y2 = list(p1['식료품'])

# # db연결 
# conn = cx_Oracle.connect("ora_user/1234@localhost:1521/XE")

# # db실행 후 메모리 선언
# cs = conn.cursor()

# #입력받은 데이터를 저장
# sql = "insert into project_category_analytics values(:1, :2, :3)"

# for i in range(len(x)):
    
# # sql구문 실행
#     cs.execute(sql,(x[i],y[i],y2[i]))

# print("insert : ", cs.rowcount)
    
# cs.close()
# conn.commit()
# conn.close()


# ####################################################################################


# #########################################################################################
# # #오라클db에 분석한 데이터 삽입############################################################
# import cx_Oracle

# #SQL로 테이블 생성
# # create table project_category_analytics (
# #     loc varchar2(20) primary key,
# #     expenditure_all  varchar2(20),
# #     expenditure_food  varchar2(20)
# # );

# x = list(p1['지역'] )
# y = list(p1['전체'] )
# y2 = list(p1['식료품'])

# # db연결 
# # conn = cx_Oracle.connect("project/Epdlxjqpdltm1!@localhost:1521/XE")

# # instantclient경로
# # cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle18\instantclient_21_3") windows
# cx_Oracle.init_oracle_client(lib_dir=r"/Users/hyeonchanglee/sw/instantclient_19_8") # 클라이언트 경로(mac)
# conn = cx_Oracle.connect(user='ADMIN', password='Epdlxjqpdltm1!', dsn='db_high')

# # db실행 후 메모리 선언
# cs = conn.cursor()

# #입력받은 데이터를 저장
# sql = "insert into project_category_analytics values(:1, :2, :3)"

# for i in range(len(x)):
    
# # sql구문 실행
#     cs.execute(sql,(x[i],y[i],y2[i]))

# print("insert : ", cs.rowcount)


# sql = "insert into project_category_analytics values(:1, :2, :3)"


    
# cs.close()
# conn.commit()
# conn.close()


# print('완료')

# # ####################################################################################
# 오라클 클라우드에서 삽입



import cx_Oracle
import jaydebeapi


cx_Oracle.init_oracle_client(lib_dir=r"/Users/hyeonchanglee/sw/instantclient_19_8") # 클라이언트 경로(mac)
# cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle18\instantclient_21_3") # 클라이언트 경로(windows)
conn = cx_Oracle.connect(user='ADMIN', password='Epdlxjqpdltm1!', dsn='db_high')

cs = conn.cursor()

#분석한 데이터를 리스트로 놓는 곳

    #     
    #     create table project_storez_raw_lhc(
    #     year varchar2(10),
    #     quarter varchar2(3),
    #     gucode_gu varchar2(10),
    #     gucode_name varchar2(50),
    #     service_code varchar2(20),
    #     store_count number(5),
    #     storeall_count number(5),
    #     store_franchise_count number(5)
    # );

#예)
# x = list(p1['지역'] )
# y = list(p1['전체'] )
# y2 = list(p1['식료품'])


#컬럼 확인
# Index(['기준_년_코드', '기준_분기_코드', '상권_코드', '상권_코드_명', '서비스_업종_코드', '점포_수',
#        '유사_업종_점포_수', '프랜차이즈_점포_수'],
#       dtype='object')

df = [tuple(x) for x in df.values] #오라클 디비에 넣기위해 df의 각 rows를 튜플 형태로 바꿔주고 리스트에 담음


year = list(df['기준_년_코드'] )
quarter = list(df['기준_분기_코드'] )
gucode_gu = list(df['상권_코드'] )
gucode_name = list(df['상권_코드_명'] )
service_code = list(df['서비스_업종_코드'] )
store_count = list(df['점포_수'] )
storeall_count = list(df['유사_업종_점포_수'] )
store_franchise_count = list(df['프랜차이즈_점포_수'] )


#입력받은 데이터를 저장
# sql = "insert into project_storez_raw_lhc values(:1, :2, :3, :4, :5, :6, :7, :8)"

sql = "insert into project_storez_raw_lhc(\
    year,\
        quarter,\
            gucode_gu,\
                gucode_name,\
                    service_code,\
                        store_count,\
                            storeall_count,\
                                store_franchise_count) values(:1, :2, :3, :4, :5, :6, :7, :8)"



for i in range(len(year)):
    
# sql구문 실행
    cs.execute(sql,(year[i],quarter[i],gucode_gu[i],gucode_name[i],service_code[i],store_count[i],storeall_count[i],store_franchise_count[i]))

print("insert : ", cs.rowcount)
    
cs.close()
conn.commit()
conn.close()







# sql ='select * from project_category_analytics'
# cs.execute(sql)
# print(cs.fetchall())

# cs.close()
# conn.close()