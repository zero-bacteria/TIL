# P,H,W - 1.19



### 실수비교

* python계산 과정에서 근사값으로 나타나는데 실수를 비교할 때 `==`을 사용하면 이러한 오류에 빠지기 쉽다.

  ```python
  import math
  
  a=0.1*3
  b=0.3
  
  print(math.isclosea,b))
  ```

* 해당 과정을 통해서 실수 비교를 할 수 있다.



### string interpolation

* 스트링 내삽 방법

  ```python
  name = '철수'
  
  answer1 = print('안녕, {}야'.format(name))
  answer2 = print(f'안녕, {name}야')
  ```

  

### 중간값 찾기

* len 함수를 이용하고 중간값이 홀수 짝수일때를 생각해야 한다.



### sort vs sorted

* `list.sort()` : 원본값을 변형시킴 빠름
* `sorted` : 원본값에는 손 안댐 느림(복사본만듬)



### print 에서 출력 참고

* 포문 돌릴때 혹은 한번에 표현할때`end=` ,`\n` ,`''` 를 사용하여 적절히 표현해보자



### mutable 쉽게 생각하기

* index를 찾아 변경할 수 있으면 mutable 아니면 immutable ? (내생각)