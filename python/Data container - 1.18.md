# Data container - 1.18



> 데이터는 크게 Sequence 와 Non-sequence 로 나뉘어 질 수 있다.



## Sequence

* 리스트, 튜플, 레인지, 문자형, 바이너리 가 있다.



### 튜플

* 수정 불가능, 내부에서 다양한 용도로 쓰임
* 다음과 같이 만들 수 있음

```python
ex_tuple = 1,2
```

```python
tuple1 = ('hello')
type(tuple1)
#str
```

* 인덱스를 이용해 튜플을 읽을수 있다. (수정은 x)



### Range

* 레인지를 통해 범위 지정 가능
* 리스트 형태로 나옴



### 시퀀스에서 사용가능한 것들

* `[:]` 슬라이싱도 레인지와 같이 범위 지정시 마지막 범위는 포함 x

  ex) [1:3] => index 1,2 까지만 포함







## Non-sequence

### set

* 순서가 없는 자료구조로 집합이라고 생각하면된다. ( 기호도 똑같음`{}`)

* 연산도 똑같은 구조로 진행된다.

* 중복되는것을 제거할 수 있는 트릭으로 쓸 수 있다.

  ```python
  list_a = [1,1,1,3,3,4,2,3,4,5,4,]
  list(set(list_a))
  # [1,2,3,4,5]  순서가 보장되는 것은 아니다.
  ```



### Dictionary

* key,value로 구성 key는 변경 불가능한 데이터만 된다.
  * immutable data : string, integer, float, boolean, tuple, range
* value는 모든것 가능
* `.keys` `.values`를 통해 확인 해 볼 수 있다. 
  * 하지만 타입은 dict_(values or keys)로 나온다.

* `.items()` 메소드를 통해 key, value를 확인 해 볼 수 있다.
  * 유사 리스트이다. 
  * 리스트로 변경해 볼 수 있다 -> `list()`사용





## 형변환

* 딕셔너리 리스트등으로 바꾸면 키값만 알려준다.
* 밸류를 알려주고 그에 맞는 키값을 찾을 수 없다.





## 데이터 분류



### immutable

* 리터럴(literal)
  - 숫자(Number)
  - 글자(String)
  - 참/거짓(Bool)
* range()
* tuple()
* ~~frozenset()~~





## 기타 참고



리스트를 같다라고 해놓으면 하나 바꾸면 둘다 바뀜



```python
a=[1,2,3,4]
b=a
a[0]=0
print(a)
print(b)
```

```
결과값
[0,2,3,4]
[0,2,3,4]
```

