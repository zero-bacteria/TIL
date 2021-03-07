N = int(input())

# a b c 순서대로 있다
# n 은 옮겨야하는 링의 개수이다.
def hanoi(n, a=1, b=2, c=3):
    
    # init 설정 
    # 결국 목표가 a에서c 로 옮기는 것 이다.
    # a는 출발지 b는 경유지 c는 도착점
    if n == 1:
        print(a, c)
    else:
        # a에서 b로 옮기는 것을 표현한것
        # why? 제일 위에것을 출발지에서 일단 경유지로 옮겨야 하기 때문
        hanoi(n-1, a, c, b)
        # 맨밑에 판을 목표했던 도착점으로 옮기는 것
        print(a, c)
        # 맨밑에 판을 옮겼으면 그곳으로 다시 옮겨놓는 과정
        hanoi(n-1, b, a, c)

        # 말이 어려울 수 있지만 쉽게 생각하면 2개 있을때를 생각해 보면 된다.
        # 맨처음에 하나 경유지에 놓고 맨밑에 판을 목적지에 놓고 다시 올려놓는과정
        # 이과정을 계속해서 반복하는 재귀함수이다.

# 총횟수는 2의 N제곱에서 1을 뺀값과 같다
# 왜냐하면 하나 늘어날수록 2배늘어나기 때문이다.

print(2**N-1)
hanoi(N)