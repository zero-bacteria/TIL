from django.shortcuts import render

# Create your views here.
# 뷰함수에서 첫번째 인자는 반드시 request
def index(request):
    # 렌더함수의 첫번째 인자도 request 여야 한다.
    # 템플릿의 경로는 반드시 templates로 작성해야 한다.
    # 왜냐하면 장고는 템플릿의 경로는 알고있다.
    # 따라서 불러올때도 다른것처럼 패키지 사용이 아닌 그냥 불러오면 된다.
    return render(request, 'index.html')

def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Harry'
    }
    context = {
        'info': info,
        'foods': foods, 
    }

    return render(request, 'greeting.html', {'name': 'Harry'})

def detail(request, article_num):
    context = {
        'article_num': article_num,
    }
    return render(request, 'detail.html', context)

def throw(request):
    return render(request, 'throw.html')