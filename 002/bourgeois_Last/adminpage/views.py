from unicodedata import category
from django.shortcuts import render,redirect
from membership.models import BourgeoisMember
import cx_Oracle as ora
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from qnaboard.models import Freeboard
from django.db.models import F,Q
from django.core.paginator import Paginator



def web_admin(request):
    return render(request,'web.html')

def fDelete(request,nowpage,f_no):
    qs = Freeboard.objects.get(f_no=f_no)
    qs.delete()
    return redirect('qnaboard:fList',nowpage)

def login_admin(request):
    if request.method == 'GET':
        print('get')
        return render(request,'login_admin.html')
    else:
        id = request.POST.get('inp_id')
        pw = request.POST.get('inp_pwd')
        print(id) #request 넘어오는지 체크
        print(pw)      
       
        if id == 'admin' and pw =='1234':
            request.session['session_ID'] =id
           
            print(id)
            return render(request,'web.html') #상단url주소가 변경되지 않음.
            # return redirect('/')

        else:
            # id,pw가 존재하지 않을 시
            msg="아이디 또는 패스워드가 일치하지 않습니다. \\n 다시 로그인해주세요.!!"
            return render(request,'login_admin.html',{'msg':msg})


# freeboard fUpdate 함수
def fUpdate(request,nowpage,f_no):
    if request.method == 'GET':
        qs = Freeboard.objects.get(f_no=f_no)
        context = {'board':qs,'nowpage':nowpage}
        return render(request,'fUpdate.html',context)
    else:
        # 수정form에서 데이터 전달
        ID = request.POST.get('id')
        if ID == 'admin':
            request.session['session_ID'] =ID
            title = request.POST.get('title')
            content = request.POST.get('content')
            file = request.FILES.get('file',None)
            print("file : ",file)
        # db에 수정저장
            qs = Freeboard.objects.get(f_no=f_no)
            qs.f_title = title
            qs.f_content = content
            if file:  # file등록이 되었으면 저장함.
                qs.f_file = file
                print("qs.f_file ok")
            qs.save()
            return redirect('adminpage:fList',nowpage)
        return redirect('adminpage:fList',nowpage)


def fWrite(request,nowpage,category,searchword):
    if request.method == 'GET':
        context={"nowpage":nowpage,'category':category,'searchword':searchword}
        return render(request,'fWrite.html',context)
    else:
        # form넘어온 데이터
        if request.POST.get("id") == 'admin': 
        
            print("ID ",request.POST.get("id"))
            member = BourgeoisMember.objects.get(ID=request.POST.get("id"))
            title = request.POST.get("title")
            content = request.POST.get("content")
            file = request.FILES.get('file',None)
            # db 저장
            qs = Freeboard('admin',f_title=title,f_content=content,f_file=file)
            qs.save()
            qs.f_group = qs.f_no
            qs.save()
            return redirect('adminpage:fList',nowpage,category,searchword)
        elif request.POST.get("id") != 'admin' :
            
            return redirect('adminpage:fList',nowpage,category,searchword)
        else:
            return redirect('adminpage:fList',nowpage,category,searchword)

 
        

    

# freeboard fView 함수
def fView(request,nowpage,f_no):
    qs = Freeboard.objects.get(f_no=f_no)
    try:
        qs_prev = Freeboard.objects.filter(f_group=qs.f_group,f_step__lt=qs.f_step).order_by('-f_group','f_step').last().f_no
    except:  
        try:
            qs_prev = Freeboard.objects.filter(f_group__gt=qs.f_group).order_by('-f_group','f_step').last().f_no
        except:
            qs_prev = Freeboard.objects.order_by('-f_group','f_step').first().f_no
   
    # 다음글
    try:
        # 답글로 게시글이 등록될때 찾을수 있는 다음글검색
        qs_next = Freeboard.objects.filter(f_group=qs.f_group,f_step__gt=qs.f_step).order_by('-f_group','f_step').first().f_no
    except:  
        # 순차적으로 게시글이 등록될대 찾을수 있는 다음글검색
        try:
            qs_next = Freeboard.objects.filter(f_group__lt=qs.f_group).order_by('-f_group','f_step').first().f_no
        except:
            # 처음 게시글 선택시 에러 처리
            qs_next = Freeboard.objects.order_by('-f_group','f_step').last().f_no
                
    print("qs_prev : ",qs_prev)
    qs.f_hit += 1
    qs.save()
    qsPrev = Freeboard.objects.get(f_no=qs_prev)
    qsNext = Freeboard.objects.get(f_no=qs_next)
    # 이전글 게시글 검색
    context={'adboard':qs,'aboardPrev':qsPrev,'boardNext':qsNext,'nowpage':nowpage}
    return render(request,'fView.html',context)

# 게시판 리스트 함수
def fList(request,nowpage,category,searchword):
    # GET,POST 포함
    # all,title,content
    if request.method =='POST':
        category = request.POST.get('category')
        searchword = request.POST.get('searchword')
        print("POST category : ",category,searchword)
    
    print("main category : ",category,searchword)
    # category분류
    if category == 'first':  # GET으로 들어옴.
        qs = Freeboard.objects.order_by('-f_group','f_step')
    elif category == 'title':
        qs = Freeboard.objects.filter(f_title__contains=searchword)
    elif category == 'content':
        qs = Freeboard.objects.filter(f_content__contains=searchword)
    else: # all
        # or 검색 : title or content
        qs = Freeboard.objects.filter(Q(f_title__contains=searchword)|Q(f_content__contains=searchword))
        # and 검색 : title and content
        # qs = Fboard.objects.filter(f_title__contains=searchword,f_content__contains=searchword)    
    
    paginator = Paginator(qs,10)     # 1페이지 나타낼수 있는 게시글 수 설정.  
    fList = paginator.get_page(nowpage) # 요청한 페이지의 게시글 10개를 전달
    print("count : ",qs.count)
    context={'fList':fList,'count':qs.count,'nowpage':nowpage,'category':category,'searchword':searchword}
    return render(request,'fList.html',context)


# def fReply(request,nowpage,category,searchword,f_no):
#     if request.method == 'GET':
#         qs = Freeboard.objects.get(f_no=f_no) 
#         context={'board':qs,'nowpage':nowpage,'category':category,'searchword':searchword}
#         return render(request,'fReply.html',context)
#     else:
        
#         ID = request.POST.get('id')
#         print("id:",ID)
#         if ID != 'admin':
#             member = BourgeoisMember.objects.get(ID=ID)
#             print('member',member)
#         request.session['session_ID'] =ID
#         print(ID)
    
#         title = request.POST.get('title')
#         content = request.POST.get('content')      
#         file = request.FILES.get('file',None)
#     # request 넘어온 데이터타입 : str타입
#         group = int(request.POST.get('group'))
#         step = int(request.POST.get('step'))
#         indent = int(request.POST.get('indent'))
#         Freeboard.objects.filter(f_group=group,f_step__gt=step).update(f_step=F('f_step')+1)
#         # step: 출력순서, indent: 들여쓰기
#         qs=Freeboard('member',f_no=f_no,f_title=title,f_content=content,f_group=group\
#             ,f_step=step+1,f_indent=indent+1,f_file=file)
#         qs.save() # f_no
#         # step: 출력순서, indent: 들여쓰기
#         qs.save()
        
#         return redirect('adminpage:fList',nowpage,category,searchword)
   
    
def list(request,nowpage,category,searchword):
    if request.method =='POST':
        category = request.POST.get('category')
        searchword = request.POST.get('searchword')
        print("POST category : ",category,searchword)
    
    print("main category : ",category,searchword)
    # category분류
    if category == 'first' or searchword =='first':  # GET으로 들어옴.
        qs = BourgeoisMember.objects.order_by('-ID')
        
    elif category == 'ID':
        qs = BourgeoisMember.objects.filter(ID__contains=searchword)
        
    elif category == 'NAME':
        qs = BourgeoisMember.objects.filter(NAME__contains=searchword)
    elif category == 'LEGION':
        qs = BourgeoisMember.objects.filter(LEGION__contains=searchword)
    elif category == 'CuriousLEGION':
        qs = BourgeoisMember.objects.filter(CuriousLEGION__contains=searchword)
    elif category == 'CuriousSECTOR':
        qs = BourgeoisMember.objects.filter(CuriousSECTOR__contains=searchword)
    else: # all
        # or 검색 : title or content
        qs = BourgeoisMember.objects.filter(Q(ID__contains=searchword)|Q(NAME__contains=searchword))
        # and 검색 : title and content
        # qs = Fboard.objects.filter(f_title__contains=searchword,f_content__contains=searchword)    
    
    paginator = Paginator(qs,10)     # 1페이지 나타낼수 있는 게시글 수 설정.  
    list = paginator.get_page(nowpage) # 요청한 페이지의 게시글 10개를 전달
    print("count : ",qs.count)
    context={'memberList':list,'count':qs.count,'nowpage':nowpage,'category':category,'searchword':searchword}
    return render(request,'list.html',context) 
    

# 게시판 읽기 함수
def fView(request,nowpage,category,searchword,f_no):
    qs = Freeboard.objects.get(f_no=f_no)
    # 게시판리스트- f_group역순정렬, f_step순차정렬
    # qs = Fboard.objects.order_by('-f_group','f_step')
    # 이전글
    try:
        # 답글로 게시글이 등록될때 찾을수 있는 이전글검색
        qs_prev = Freeboard.objects.filter(f_group=qs.f_group,f_step__lt=qs.f_step).order_by('-f_group','f_step').last().f_no
    except:  
        # 순차적으로 게시글이 등록될대 찾을수 있는 이전글검색
        try:
            qs_prev = Freeboard.objects.filter(f_group__gt=qs.f_group).order_by('-f_group','f_step').last().f_no
        except:
            # 마지막 게시글 선택시 에러 처리
            qs_prev = Freeboard.objects.order_by('-f_group','f_step').first().f_no
    
    # 다음글
    try:
        # 답글로 게시글이 등록될때 찾을수 있는 다음글검색
        qs_next = Freeboard.objects.filter(f_group=qs.f_group,f_step__gt=qs.f_step).order_by('-f_group','f_step').first().f_no
    except:  
        # 순차적으로 게시글이 등록될대 찾을수 있는 다음글검색
        try:
            qs_next = Freeboard.objects.filter(f_group__lt=qs.f_group).order_by('-f_group','f_step').first().f_no
        except:
            # 처음 게시글 선택시 에러 처리
            qs_next = Freeboard.objects.order_by('-f_group','f_step').last().f_no
    
            
    print("qs_prev : ",qs_prev)
    qs.f_hit += 1
    qs.save()
    qsPrev = Freeboard.objects.get(f_no=qs_prev)
    qsNext = Freeboard.objects.get(f_no=qs_next)
    # 이전글 게시글 검색
    context={'board':qs,'boardPrev':qsPrev,'boardNext':qsNext,'nowpage':nowpage,'category':category,'searchword':searchword}
    return render(request,'fView.html',context)
    


def makeDictFactory(cursor):
    columnNames = [d[0] for d in cursor.description] 
    def createRow(*args):
        return dict(zip(columnNames,args))
    return createRow 

def members(request):
    conn= connections()
    cursor = conn.cursor()
    cursor.execute("select * from BOURGEOISMEMBER")

    cursor.rowfactory = makeDictFactory(cursor)
    rows = cursor.fetchall()
    conn.close()
    context={'memberList':rows}
    return render(request,'web.html',context)

def connections():
    try:
       conn = ora.connect('ora_pro/1234@localhost:1521/xe')
    except:
        print('error')
        
    return conn   

#####logout함수
def logout(request):
    request.session.clear()
    return redirect('/')

def memberDelete(request,ID):
   
    qs = BourgeoisMember.objects.get(ID=ID)
    qs.delete()
    return redirect('adminpage:list',nowpage=1,category='first',searchword='first')
    

def memberView(request,ID):
    qs = BourgeoisMember.objects.get(ID=ID)
    context = {'member':qs}
    return render(request,'memberView.html',context)
 