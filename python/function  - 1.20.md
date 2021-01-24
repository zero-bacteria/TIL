# function  - 1.20





### parameter , argument

* 함수내부에서 활용할 변수 parameter

* 호출할때 사용하는 변수 argument

  

  

### argument





#### 위치인자

일반 인자로 위치를 바꾸면 값다르게 나옴



#### 기본인자

함수가 호출될 때 인자를 지정하지 않아도 기본값 설정 가능

**but** 기본인자 값이 존재할때는 기본값이 없는 인자를 넣을 수는 없다.

```python
def greeting(age, name='익명'):
    print(f'안녕? 난{name}, {age}살이야')]
    
    greeting(name='길동', age=1000)
```

```python
greeting(age=3000, '곰')
```





### *args



* `*args`를 이용할때 앞에올수 는 없고 뒤에는 상관없다.

```python
def x(a,args*)  # O
def x(args*,a)  # X
```



### *kwargs 



* 딕셔너리 형태로 입력받은것을 처리할 수 잇는 함수이다.

* 딕셔너리 형태의 포문을 돌릴때

  ```python
  for name, value in kwargs.items():
  ```



## 함수와 스코프



전역이 먼저이다.

* 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있습니다.

  이것을, `LEGB Rule` 이라고 부르며, 아래와 같은 순서로 이름을 찾아나갑니다.

  - `L`ocal scope: 정의된 함수

  - `E`nclosed scope: 상위 함수

  - `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈

  - `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성





## 재귀함수

자기 자신을 호출하는 함수

* 재귀함수를 작성시에는 무조건 basecase 머저 설정해주자
* 최대 재귀 깊이는 3000
* 재귀함수 이해가 어려우면 그림그려가면서 풀어보기
* 재귀함수는 반복문에 비해 점화식과 같은 구조파악이 쉬우며 변수가 적게 들어간다.
* 

