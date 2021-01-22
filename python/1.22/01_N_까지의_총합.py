'''
N 까지의 총합

정수 num을 기준으로, 1~num까지의 총 합을 구하는 함수를

1. `for` 문을 사용하여
2. `while`문을 사용하여

작성하시오.
'''

# for문만 사용하여 풀기

def sum_with_for(num):
    # 변수 초기화
    result = 0
    # 범위 지정 반복문을 통한 합
    for i in range(1,num+1):
        result+= i
        
    return result

print(sum_with_for(4))
    

# while문만 사용하여 풀기
def sum_with_while(num):
    # 변수 초기화
    result=0
    # while 범위 지정 변수 초기화
    n=1
    # 반복을 통한 결과값의 합
    while n<num+1:
        result+=n
        n+=1
    return result

print(sum_with_while(5))
    


# 아래 코드는 바꾸지 않습니다.
if __name__ == '__main__':
    print(sum_with_for(4))    # 10
    print(sum_with_while(4))  # 10
    print(sum_with_for(5))    # 15
    print(sum_with_while(5))  # 15