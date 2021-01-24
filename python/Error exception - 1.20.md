# Error exception - 1.20



## try except

* try - except 를 통해 예외처리를 할 수 있다.

* try에 사용할 코드

* except에 예외로 발생할 케이스를 넣는다.

  ```python
  try: 
      num = input('값을 입력하시오 : ')
      print(int(num))
  except ValueError:
      print('숫자를 입력하라니까!!')
  ```

  

* as를 통해 에러메세지를 남겨 줄 수 있다.
* 여러가지 예외 케이스가 있으면 그냥 except를 또 쓰면 된다.



### else

* try - except 에서 예외 케이스가 발생하지 않는다면 else문이 수행된다.
* 모든 except 뒤에 와야한다.



### finally

* 반드시 수행되는 문장이다.
* 모든상황에서 실행되는 코드로 실행, 에러와 상관없이 try 문을 떠날대 실행되는 것 이다.



## raise 

* 에러를 발생시키는 경우이다.