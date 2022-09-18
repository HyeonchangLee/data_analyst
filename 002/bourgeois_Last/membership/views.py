from django.shortcuts import redirect, render
import cx_Oracle as ora
import json
from django.http import JsonResponse
#####가입, 로그인관련 Django 내부 함수.
from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
##### 로그인 함수.
from membership.models import BourgeoisMember


#######회원가입페이지 함수.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    else:
        try:
            id = request.POST.get('inp_id')
            qs = BourgeoisMember.objects.get(ID=id)
            msg ="이미 존재하는 아이디입니다."            
            return render (request, 'signup.html', {'msg':msg})
        except:

            if request.POST['inp_pwd'] == request.POST['inp_repwd']:
                
                id = request.POST.get('inp_id')
                pw = request.POST.get('inp_pwd')
                name = request.POST.get('inp_name')
                age = request.POST.get('inp_AGE')
                gender = request.POST.get('inp_gender')
                legion = request.POST.get('inp_LEGION')
                curiouslegion = request.POST.get('inp_CuriousLEGION')
                curioussector = request.POST.get('inp_CuriousSECTOR')
                # db에 저장 -> table insert명령어
                BourgeoisMember.objects.create(ID=id,PW=pw,NAME=name,AGE=age,GENDER=gender,LEGION=legion,CuriousLEGION=curiouslegion,CuriousSECTOR=curioussector)
                print("insert OK!")
                
                return HttpResponseRedirect(reverse('membership:login'))
            else:
                msg = "비밀번호와 비밀번호 확인이 일치하지 않습니다.\\n 다시 확인하시고 가입하시기 바랍니다."
                return render (request, 'signup.html', {'msg':msg})



#######마이페이지 함수.
def mypage(request):
    return render(request,'mypage.html')




################# 오라클 클라우드 사전 절차 진행 후 주석 해제할것
# oracle db연결 (클라우드)

def connections():
    try:
        conn = ora.connect(user='ADMIN', password='Epdlxjqpdltm1!', dsn='DBseoul_high')
    except:
        print('error')
        
    return conn   

def makeDictFactory(cursor):
    columnNames = [d[0] for d in cursor.description] 
    def createRow(*args):
        return dict(zip(columnNames,args))
    return createRow 


####로그인시 회원테이블에서 DB 연결함수.

def members(request):
    conn= connections()
    cursor = conn.cursor()
    cursor.execute("SELECT * from MEMBERSHIP_BOURGEOISMEMBER;")



#####로그인 함수
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        id = request.POST.get('inp_id')
        pw = request.POST.get('inp_pwd')
        # print(id) #request 넘어오는지 체크
        # print(pw)
        
        try:
            # id, pw가 존재할 시
            qs = BourgeoisMember.objects.get(ID=id,PW=pw)
        except BourgeoisMember.DoesNotExist:
            qs = None
        
        if qs:
            request.session['session_ID'] = qs.ID
            request.session['session_NAME'] = qs.NAME
            request.session['session_AGE'] = qs.AGE
            request.session['session_GENDER'] = qs.GENDER
            request.session['session_LEGION'] = qs.LEGION
            request.session['session_CuriousLEGION'] = qs.CuriousLEGION
            request.session['session_CuriousSECTOR'] = qs.CuriousSECTOR
            print(qs.ID)
            print(qs.CuriousSECTOR)

            # return render(request,'web.html') #상단url주소가 변경되지 않음.
            return redirect('/')
        elif id == 'admin' and pw =='1234':
            request.session['session_ID'] = id
            
            print(id)
            return render(request,'web_admin.html')

        else:
            # id,pw가 존재하지 않을 시
            msg="아이디 또는 패스워드가 일치하지 않습니다. \\n다시 확인하시고 로그인 해주세요."
            return render(request,'login.html',{'msg':msg})








#####logout함수
def logout(request):
    request.session.clear()
    return redirect('/')



#####회원 수정 함수

def signupModify(request):
    return render(request,'signupModify.html')


#####회원 수정 OK(저장) 함수

def signupModifyOK(request):
    if request.method == 'POST':
        id = request.POST.get('inp_id')
        # print(id) #id 넘어오는지 확인.
        name = request.POST.get('inp_name')
        age = request.POST.get('inp_AGE')
        gender = request.POST.get('inp_gender')
        legion = request.POST.get('inp_LEGION')
        curiouslegion = request.POST.get('inp_CuriousLEGION')
        curioussector = request.POST.get('inp_CuriousSECTOR')

        
        # s_no 데이터 찾기
        qs = BourgeoisMember.objects.get(ID=id)
        qs.NAME = name
        qs.AGE = age
        qs.GENDER = gender
        qs.LEGION = legion
        qs.CuriousLEGION = curiouslegion
        qs.CuriousSECTOR = curioussector
        # 데이터 수정저장
        qs.save()
        
        return HttpResponseRedirect(reverse('membership:login'))


#####회원 삭제 함수

def memberDelete(request):
    if request.method == "GET":
        id = request.session['session_ID']
        qs = BourgeoisMember.objects.get(ID=id)
        qs.delete()
        request.session.clear()
        return redirect('/')
    
  
    


    
#####MY분석 페이지 오픈 함수
def myApageopen(request):
    return render (request, 'myApage.html')