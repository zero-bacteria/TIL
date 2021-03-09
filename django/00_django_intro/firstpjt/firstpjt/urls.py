"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# 수많은 url 들을 묶어오기 위한 include 사용
from django.urls import path, include
# include 사용하면서 옮김
# # view에 있는 함수를 사용하기 위해서 패키지 처럼 접근
# from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 'articles/'로 시작하는 주소는 articles 앱의 urls.py에 가서 처리해!
    path('articles/', include('articles.urls'))
    # 원래 했던거를 include 사용하면서 올김
    # path('index/', views.index),
    # path('greeting/', views.greeting),
]
