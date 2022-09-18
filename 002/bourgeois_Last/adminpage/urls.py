from . import views
from django.urls import path,include

app_name = 'adminpage'
urlpatterns = [
    # path('memberList/', views.memberList, name='memberList'),
    path('web_admin',views.web_admin,name='web_admin'),
    path('login_admin/',views.login_admin,name='login_admin'),
    path('logout/',views.logout, name= 'logout'),
    
  
    path('<int:nowpage>/<str:category>/<str:searchword>/list/',views.list, name='list'),
    path('<int:nowpage>/<str:category>/<str:searchword>/fList/',views.fList,name='fList'),
    path('<int:nowpage>/<str:category>/<str:searchword>/fWrite/',views.fWrite,name='fWrite'),
  
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fView',views.fView,name='fView'),
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fDelete',views.fDelete,name='fDelete'),
   
   
    path('<str:ID>/memberView/',views.memberView,name='memberView'),
    path('<str:ID>/memberDelete/',views.memberDelete, name='memberDelete'),
        
]
