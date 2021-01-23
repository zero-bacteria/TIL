# Control flow - 1.18

 흐름제어에 관한 내용



## 조건문

* 삼항 연산자 방법으로 조건문 표현 가능, `:` 를 생략하고 씀

  ```python
  true_value if <조건식> else false_value
  ```

  ```python
  num = int(input())
  value = num if num>=0 else -num
  print(value)
  ```

  

## 반복문

* `enumerate()`를 활용하여 인덱스와 같이 출력할 수 있다.

* 튜플형식으로 출력된다.

  ```python
  for idx, menu in enumerate(lunch):
      print(idx,menu)
  ```

  ```python
  for idx, menu in enumerate(lunch, start=1):
      print(idx, menu)
      # 1부터 나옴
  ```



### 반복제어

* break 문은 for나 while 에서 빠져나간다.
* if에서 조건문을 활용하면 된다.
* else 문이 반복문에서 쓰일수있다.
  * 반복에서 리스트의 소진이나 (`for` 의 경우) 조건이 거짓이 돼서 (`while` 의 경우) 종료할 때 실행된다.
  * 하지만 반복문이 **`break` 문으로 종료될 때는 실행되지 않는다.** (즉, `break`를 통해 중간에 종료되지 않은 경우만 실행)

* continue 는 건너뛰는 개념