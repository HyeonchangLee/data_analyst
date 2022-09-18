from . import views
from django.urls import path,include

app_name = 'navertrend'
urlpatterns = [
    path('search_page/', views.search_page, name='search_page'),
    path('search_kwd/', views.search_kwd, name='search_kwd'),
    # path('search_ad_api/', views.search_ad_api, name='search_ad_api'),
]
