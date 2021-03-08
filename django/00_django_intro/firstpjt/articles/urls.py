from django.urls import path
from . import views

# 'articles/'로 시작하는 주소를 처리
urlpatterns = [
    # 'articles/index/'로 요청했을 경우 뷰 함수의 index 수행
    path('index/', views.index),

    # 'articles/1/'로 요청했을 경우 뷰 함수의 detail 수행
    path('<int:article_num>/', views.detail),

    path('greeting/', views.greeting),

    path('throw/', views.throw),

]
# url을 분류해서 처리해주는 작업?
