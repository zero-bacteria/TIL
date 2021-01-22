'''
리스트의 총곱

사용자가 입력한 정수 num을 기준으로, 1~num으로 이루어진 리스트의 총 곱을 구하는 함수를

1. `for`문을 사용하여
2. `while`문을 사용하여

작성하시오.
'''

# for문만 사용하여 풀기
def mul_with_for(numbers):
    numbers_list =[]
    result = 1
    for i in range(1,numbers+1):
        numbers_list += [i]
    
    for number in numbers_list:
        result*= number
        
    return result

 
print(mul_with_for(4))    


# while문만 사용하여 풀기
def mul_with_while(numbers):
    numbers_list =[]
    result = 1
    a=1
    while a<=numbers :
        numbers_list += [a]
        a +=1
    n=0
    while n<numbers:
        result*=numbers_list[n]
        n+=1
    return result
    
print(mul_with_while(5))


# # 아래 코드는 바꾸지 않습니다.
# if __name__ == '__main__':
#     num = int(input('정수를 입력하세요'))
#     numbers = list(range(1, num+1))

#     # 아래 두코드 모두 in 4 => out 24 / in 5 => out 120 를 만족해야 합니다.
#     print(mul_with_for(numbers))
#     print(mul_with_while(numbers))