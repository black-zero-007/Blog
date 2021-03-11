# Author:JZW
from django.urls import path,re_path
from blog import views
urlpatterns = [
    path('up_down/', views.up_down),
    path('comment/', views.Comment),
    re_path('backend/add_article/(\w+)/$',views.add_article),
    re_path('(\w+)/article/(\d+)/$',views.article_detail),
    re_path('(\w+)/$',views.home),


]