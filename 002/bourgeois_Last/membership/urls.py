from . import views
from django.urls import path,include

app_name = 'membership'
urlpatterns = [
    # path('memberList/', views.memberList, name='memberList'),
    #회원 나의 페이지
    path('mypage/',views.mypage,name='mypage'),
    #회원 로그인 페이지
    path('login/',views.login,name='login'),
    #회원 로그아웃
    path('logout/',views.logout, name= 'logout'),
    #회원 가입 페이지
    path('signup/',views.signup,name='signup'),
    #회원 나의 페이지 -> 회원정보변경 페이지로 이동
    path('signupModify/',views.signupModify, name='signupModify'),
    #회원정보변경완료 및 DB 저장.
    path('signupModifyOK/',views.signupModifyOK, name='signupModifyOK'),
    #회원 탈퇴.
    path('memberDelete/',views.memberDelete, name='memberDelete'),
    #mypage open.
    path('myApageopen/', views.myApageopen, name='myApageopen'),
    
]
