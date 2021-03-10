from django.db import models

# Create your models here.

class Article(models.Model):
    # CharField, TextField
    # 필수 인자 존재(문자열 길이 제한)
    title = models.CharField(max_length=30) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 데이터 베이스의 테이블을 만들기위한 모델링 과정
    # 어떠한 명령을 보내줘야 실제로 article 이라는 테이블이 생김

    # 모델링을 한 뒤 수행하는 루틴
    
