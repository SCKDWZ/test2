

from django.urls import path
from .views import *
urlpatterns=[
    path('index/',Index,name='index'),
    path('blogslist/',Blogslist,name='blogslist'),
    path('bloginfo/<int:pk>/',Bloginfo,name='bloginfo'),
    path('addcomments/<int:pk>/',AddComments,name='addcomments')#新增评论
]