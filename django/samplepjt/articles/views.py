from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    # # 제대로 들고온다음 파이썬 언어로 해결
    # articles = Article.object.all()[::-1]
    # DB 단에서 해결
    articles = Article.object.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 1. GET 요청으로 들어온 사용자 데이터를 추출한다.
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 2. Article 모델 클래스를 기반으로 인스턴스를 만든다.
    # 이때, 전달받은 사용자 데이터를 넘겨주고 초기화한다.
    article = Article(title=title, content = content)

    # 3. DB에 저장한다.
    article.save()

    return render(request, 'articles/create.html')