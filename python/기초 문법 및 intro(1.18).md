# 기초문법(intro) - 1월 18일 복습 



> 유투브 강의를 들으면서 몰랐거나 확실하지 않았던 개념에 대해서 복습



* jupyter notebook 은 repl 중의 하나이다.
* IDLE 하고는 환경도 다르고 단축키도 다르다.







## 기초문법



* 여러줄 문자열은 `"""` 을 통해서 작성 (PEP-8 guide)

* 동시에 두개의 변수 선언과 해당 값을 바꿀 수 있다.

  ```python
  x,y = 10, 20
  ```

* 다음과 같이 사용 불가능한 식별자를 볼 수 있다.(내장함수)

  ``` python
  import keyword
  print(keyword.kwlist)
  ```

* 다음글은 한번 다시 읽어보자

  ---

  **파이썬에서 표현할 수 있는 가장 큰 수**

  - 파이썬에서 가장 큰 숫자를 활용하기 위해 sys 모듈을 불러온다.
  - 파이썬은 기존 C 계열 프로그래밍 언어와 다르게 정수 자료형(integer)에서 오버플로우가 없다.
  - 임의 정밀도 산술(arbitrary-precision arithmetic)을 사용하기 때문이다.

  > **오버플로우(overflow)**

  - 데이터 타입 별로 사용할 수 있는 메모리의 크기가 제한되어 있다.
  - 표현할 수 있는 수의 범위를 넘어가는 연산을 하게 되면, 기대했던 값이 출력되지 않는 현상, 즉 메모리가 차고 넘쳐 흐르는 현상

  > **임의 정밀도 산술(arbitrary-precision arithmetic)**

  - 사용할 수 있는 메모리양이 정해져 있는 기존의 방식과 달리, 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태
  - 특정 값을 나타내는데 4바이트가 부족하다면 5바이트, 더 부족하면 6바이트까지 사용할 수 있게 유동적으로 운용







## 데이터타입

* 지수표현은 컴퓨터식 지수표현을 사용할 수 있다. `1.4e-2` / `1.4E-2` 둘다 가능

* 파이썬을 사용하다보면 실제값과 다르게 나올 수 가 있다.


따라서 다음과 같은 방법으로 처리 할 수 있다. (이외에 다양한 방법이 있음)

```python
a = 3.5 - 3.12
b = 0.38

abs(a - b) <= 1e-10
```

```python
True
```

```python
# 2. sys 모듈을 통해 처리하는 방법을 알아봅시다.
# `epsilon` 은 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환
```

```python
import sys
abs(a - b) <= sys.float_info.epsilon
```

```
True
```

```python
# 3. python 3.5부터 활용 가능한 math 모듈을 통해 처리하는 법을 알아봅시다.
```

```python
import math
math.isclose(a, b)
```

```python
True
```

---

### 복소수 (complex number)



* 각각 실수부와 허수부가 있으며 `1+2j` 와 같이 표현된다

* 아래와 같이 타입은 complex 타입이다.

``` python
  a = 3-4j
  type(a)
  
  #clmplex
```

* 복소수는 `.real` r그리고 `.imag`를 사용하여 실수부와 허수부를 구분할 수 있다.

  ``` python
  complex_number = a + bj
  
  print(complex_number.real)
  print(complex_number.imag)
  
  # 1.0 ,2.0
  ```

  



---



## 문자타입

* 문자열을 묶을 때 하나로 통일하기 `'`, `"` 혼용 x

* 문자열 안에 `'`,`\` 사용시 `\`를 **앞에** 입력해 활용할 수 있다. 

  ``` python
  #ex)
  print('교수님이 말했다. \'복습은중요해!\'')
  ```

  String interpolation

```python
name = 'david'
hobby = 'singing'

print('Hi, my name is {}. My hobby is {}' .format(name,hobby))
print(f'Hi, my name is {name}. My hobby is {hobby})
```

---

### 참거짓 타입



* 참/거짓을 Boolean 이라고 한다.

  * 0, 비어있는것, none 등은 false
  * 시험시 '0'과 같은 트릭에 주의 (True)
  * bool()과 같은 내장함수로 알아낼 수 있다.
  * 일반적으로 그냥 쓰일 수 있는 경우들이 많다.
* True와 같은 값은 일반값과 계산 가능!
* 아무것도 없는 None 타입이 존재한다.



### 형변환



* 같은 형태끼리 이어 붙여야한다.

* ```python
  str(1)+'등'  # 1등
  ```

  

  

  

## 연산

* `and`, `or` 과 같은 논리연산자가 오면 무조건 논리연산으로 생각

* 괄호먼저 무조건 시행 

  ```python
  ('a' and 'b') #'b'
  ('a' or 'b') #'a'
  vowels = 'aeiou'
  ('a' and 'b') in vowels  #False
  ```
  
* `in` 연산자를 통해 요소가 속해있는지 여부를 확인 할 수 있다.

* `is` 연산자를 통해 동일한 object인지 확인 할 수 있다.

  * 파이썬에서 `-5 ~ 256` 의 id는 동일하다.
  * 같은 값을 가지고 있더라도 id는 다를 수 있다.
  * 공백없는 알파벳 문자열도 id는 동일하다.

`[:]`를 통해서 리스트를 슬라이싱(자를) 할 수 있다.

---

* **연산자 우선순위**

1. `()`을 통한 grouping
2. Slicing
3. Indexing
4. 제곱연산자 `**`
5. 단항연산자 `+`, `-` (음수/양수 부호)
6. 산술연산자 `*`, `/`, `%`
7. 산술연산자 `+`, `-`
8. 비교연산자, `in`, `is`
9. `not`
10. `and`
11. `or`

---

* 하나의 값도 문장이 될 수 있다.

  ```python
  #ex
  '이것도 문장이 될 수 있다.'
  ```

  