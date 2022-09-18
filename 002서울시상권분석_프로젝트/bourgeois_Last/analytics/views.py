from django.shortcuts import render
import cx_Oracle as ora
import json
from django.http import JsonResponse

# Create your views here.

################# 오라클 클라우드 사전 절차 진행 후 주석 해제할것
# oracle db연결 (클라우드)
y = ''
def connections():
    try:
        # instantclient경로
        # conn = ora.connect(user='ADMIN으로 고정', password='데이터베이스 비밀번호', dsn='데이터베이스이름_high') #windows
        # conn = ora.connect(user='ADMIN', password='Epdlxjqpdltm1!', dsn='db01_high') #windows (예제)
        # conn = ora.connect(user='ADMIN', password='Epdlxjqpdltm1!', dsn='dbseoul_high') #windows (예제)
        conn = ora.connect(user='ADMIN', password='Epdlxjqpdltm1!', dsn='db01_high') #mac
    except:
        print('error')
        
    return conn   

def makeDictFactory(cursor):
    columnNames = [d[0] for d in cursor.description] 
    def createRow(*args):
        return dict(zip(columnNames,args))   
    return createRow 

#################


def inner(request):
    return render(request, 'inner.html')

def hidden_game(request):
    return render(request, 'hidden_game.html')

def chart_main(request): #서울시 전체 매출 추이

    #추정매출에서 데이터 꺼내옴
    conn = connections()
    cursor = conn.cursor() 
    cursor.execute("select * from 추정매출 order by '년도','분기','지역' DESC ")
    
    # list(튜플)형태를 dic타입으로 변경
    cursor.rowfactory = makeDictFactory(cursor)
    
    rows = cursor.fetchall()
    conn.close()
    context ={'chart_main':rows}
    
    return JsonResponse(context,safe=False)


def chart_data(request):
    # 추정 매출
    if 'mapname' in request.GET:
        
        global y
        y=request.GET['mapname']

        print(y)
    print(y)
    conn = connections()
    cursor = conn.cursor() 
    cursor.execute("select * from 추정매출상세 where 지역=(:x) order by 년도, 분기, 서비스업종" ,x=y)
    
    # list(튜플)형태를 dic타입으로 변경
    cursor.rowfactory = makeDictFactory(cursor)
    
    rows = cursor.fetchall()
    conn.close()
    # 상주인구
    conn = connections()
    cursor = conn.cursor() 
    cursor.execute("select * from 상주인구 where 지역=(:x) order by 년도 ,분기",x=y)
    
    # list(튜플)형태를 dic타입으로 변경
    cursor.rowfactory = makeDictFactory(cursor)
    
    rows_2 = cursor.fetchall()
    conn.close()
    
    # 상주인구
    conn = connections()
    cursor = conn.cursor() 
    cursor.execute("select * from 추정매출 where 지역=(:x) order by 년도 ,분기",x=y)
    
    # list(튜플)형태를 dic타입으로 변경
    cursor.rowfactory = makeDictFactory(cursor)
    
    rows_21 = cursor.fetchall()
    conn.close()
    
    # 점포
    conn = connections()
    cursor = conn.cursor() 
    cursor.execute("select * from 점포 where 지역=(:x) order by 년도 ,분기 ,서비스업종",x=y)
    
    # list(튜플)형태를 dic타입으로 변경
    cursor.rowfactory = makeDictFactory(cursor)
    
    rows_3= cursor.fetchall()
    conn.close()
    
    conn = connections()
    cursor = conn.cursor() 
    cursor.execute("select * from 추정매출 order by '년도','분기','지역' DESC ")
    
    # list(튜플)형태를 dic타입으로 변경
    cursor.rowfactory = makeDictFactory(cursor)
    
    rows_4 = cursor.fetchall()
    conn.close()
    conn = connections()
    cursor = conn.cursor() 
    cursor.execute("select * from 추정매출 order by '년도','분기','지역' DESC ")
    
    # list(튜플)형태를 dic타입으로 변경
    cursor.rowfactory = makeDictFactory(cursor)
    
    rows_5 = cursor.fetchall()
    conn.close()
    
        #추정매출에서 데이터 꺼내옴
    conn = connections()
    cursor = conn.cursor() 
    cursor.execute("select * from 추정매출 order by '년도','분기','지역' DESC ")
    
    # list(튜플)형태를 dic타입으로 변경
    cursor.rowfactory = makeDictFactory(cursor)
    
    rows_6 = cursor.fetchall()
    conn.close()
    
    conn = connections()
    cursor = conn.cursor() 
    cursor.execute("select * from 추정매출 order by '년도','분기','지역' DESC")
    
    # list(튜플)형태를 dic타입으로 변경
    cursor.rowfactory = makeDictFactory(cursor)
    
    rows_7 = cursor.fetchall()
    conn.close()
    
    #rows 8 # 주말 주중 매출
    conn = connections()
    cursor = conn.cursor() 
    cursor.execute("select * from 추정매출 where 지역=(:x) order by '년도' ,'분기' ",x=y)
    
    # list(튜플)형태를 dic타입으로 변경
    cursor.rowfactory = makeDictFactory(cursor)
    
    rows_8 = cursor.fetchall()
    conn.close()
    
    #rows 9 # 주말 주중 생활인구
    conn = connections()
    cursor = conn.cursor() 
    cursor.execute("select * from 생활인구 where 지역=(:x) order by '년도','분기' ",x=y)
    
    # list(튜플)형태를 dic타입으로 변경
    cursor.rowfactory = makeDictFactory(cursor)
    
    rows_9 = cursor.fetchall()
    conn.close()
    
    #rows 10# 주말 주중 직장인구
    conn = connections()
    cursor = conn.cursor() 
    cursor.execute("select * from 직장인구 where 지역=(:x) order by '년도','분기' ",x=y)
    
    # list(튜플)형태를 dic타입으로 변경
    cursor.rowfactory = makeDictFactory(cursor)
    
    rows_10 = cursor.fetchall()
    conn.close()
    guname={'지역':y}
    context ={'aList':rows,'bList':rows_2,'b2List':rows_21,'cList':rows_3,'main_a1':rows_4, 'main_a2':rows_5, 'main_a3':rows_6, 'main_a0':rows_7,
              'dList':rows_8,'eList':rows_9,'fList':rows_10,"guname":guname}
    
    return JsonResponse(context,safe=False)


guname = ''
clegion = ''
csector = ''

#my 분석 페이지 그래프 함수 (화면의 그래프 나오는 순서와 반대로 row번호 되어 있음)
def myAPage(request):
    if request.method == "GET":
        
        global guname
        global clegion
        global csector
        
        guname = request.session['session_LEGION']
        clegion = request.session['session_CuriousLEGION']
        csector = request.session['session_CuriousSECTOR']
        

        # print('생활권 : ',guname) #request.session print test
        # print('관심지역 : ',clegion)
        # print('관심업종 : ',csector)
        
        # 관심지역 업종별 매출 myChart2
        conn = connections()
        cursor = conn.cursor() 
        cursor.execute("select * from 추정매출상세 where 지역=(:x) order by 년도, 분기, 서비스업종" ,x=clegion)
        cursor.rowfactory = makeDictFactory(cursor)
        rows = cursor.fetchall()
        conn.close()
        
        # 우리지역 업종별 매출 myChart2_1
        conn = connections()
        cursor = conn.cursor() 
        cursor.execute("select * from 추정매출상세 where 지역=(:x) order by 년도, 분기, 서비스업종" ,x=guname)
        cursor.rowfactory = makeDictFactory(cursor)
        rows_1 = cursor.fetchall()
        conn.close()
    #################################################################################################################    
        if csector == '한식':
            csector = 'CS100001'
        elif csector =='중식':
            csector = 'CS100002'
        elif csector =='일식':
            csector = 'CS100003'
        elif csector =='양식':
            csector = 'CS100004'
        elif csector =='제과점':
            csector = 'CS100005'
        elif csector =='패스트푸드점':
            csector = 'CS100006'
        elif csector =='치킨':
            csector = 'CS100007'
        elif csector =='분식':
            csector = 'CS100008'
        elif csector =='호프-간이주점':
            csector = 'CS100009'
        elif csector =='커피-음료':
            csector = 'CS100010'
            
        print(csector)
    
        # 최근 관심업종 지역별 매출 비교
        conn = connections()
        cursor = conn.cursor() 
        cursor.execute("select * from 추정매출상세 where 서비스업종=(:x) order by 년도, 분기, 지역" ,x=csector)
        cursor.rowfactory = makeDictFactory(cursor)
        rows2 = cursor.fetchall()
        conn.close()
        
        ########################################################################################################################
        # 최근 관심지역 관심업종 점포수 변화
        conn = connections()
        cursor = conn.cursor() 
        cursor.execute("select * from 점포 where (지역=(:x) and 서비스업종=(:y))  order by 년도 ,분기 ,서비스업종",x=clegion,y=csector)
        cursor.rowfactory = makeDictFactory(cursor)
        rows3= cursor.fetchall()
        conn.close()
        
        # 최근 우리지역 관심업종 점포수 변화
        conn = connections()
        cursor = conn.cursor() 
        cursor.execute("select * from 점포 where (지역=(:x) and 서비스업종=(:y))  order by 년도 ,분기 ,서비스업종",x=guname,y=csector)
        cursor.rowfactory = makeDictFactory(cursor)
        rows4= cursor.fetchall()
        print(rows4)
        conn.close()
        
        
        context = {'curiouslegion': rows, 'Ourlegion' : rows_1, 'curioussector':rows2, 'curiouslegion_shop': rows3,
                   'curiouslegion_shop_our': rows4}
        # print('받아온 데이터1 : ',rows) #데이터 체크용
        # print('#'*100)
        # print('받아온 데이터2 : ',rows2)
        
        return JsonResponse(context, safe=False)