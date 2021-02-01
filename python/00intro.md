# 과목 평가 대비 정리

> 수업 진행했던 순서대로 쭉 가면서 정리 해봄 



## intro 

* `""'`로 여러줄 글 만들기 가능

*  파이썬 코드는 1줄에 1문장 원칙

* `\`를 이용하면 붙여서 쓸수 있는데 잘 안씀

  ```python
  print('asdf\
       asdf')
  ```

* 동시에 두개의 변수에 값 두개 할당 가능

  ```python
  x, y = 10, 2
  ```

* 식별자 = Identifiers
  * 변수, 모듈, 클래스를 식별되는 이름
  * 그냥 이름이라고 생각하고 특징들 생각해보기
* 파이썬의 integer 에서는 overflow가 존재하지 않는다.
* 임의 정밀도 산술 (arbitrary-precision arithmetic)을 사용하기 때문
  * 사용할 수 있는 메모리 양이 정해져 있는 것이 아닌 유동적으로 사용

* 지수 표현 방식은 그냥 e3 이런식으로 쓰면 됨

* 실수를 연산할때 값이 다르게 나올 수도 있다. 

  * 이때 해결 방법은

    ```python
    import math
    math.isclose(a,b)
    ```

  * round를 써서 겉으로 보이는 값은 같게 만들수 있지만 실제는 아니기 때문에 저런 함수를 사용해서 Ture 값을 만들어 줄 수 있다.

* PEP-8 에 따르면 여러줄 출력은 반드시 `"""`

* 포매팅 주로 스트링 포맷 혹은 f스트링 씀

  * ```python
    print('Hi, my name is {}'.format(name))
    ```

  * ```python
    print(f'Hi, my name is {name}')
    ```

* boolean 간단정리
  * 0은 Flase
  * 비어있는 문자열,리스트,딕셔너리,튜블 모두 False
  * None 은 False
  * 뭐가 있으면 True

* boolean 은 integer안에 포함되는 개념이라고 생각하면됨

  * 1은 True
  * 0은 False

* 형변환 에서는 이것만 기억하면 됨 

  ```python
  a= '3.5'
  int(a)
  ```

  * 위에처럼하면 안됨

* 단축 평가 함정에 빠지지 않기

  * and, or 같은 것이 나오면 논리 연산이다는것!
  * 논리연산에서는 존재하면 True 아니면 False
  * and는 뒤에까지 검사해서 뒤에것이 반영
  * or는 앞에만 검사하면 되니까 가장 먼저 통과한것 반영

* list와 str은 더할수 없다.

* 공백이 없는 알파벳 문자열 id 같음 -5~256 id 같음

* [:]슬라이싱 가능

* 연산자 우선순위

  1. 괄호
  2.  slicing
  3. indexing
  4. 산술연산
  5. 비교연산, in, is
  6. 논리연산

* 하나의 값도 문장이 될수 있다!









## data container



