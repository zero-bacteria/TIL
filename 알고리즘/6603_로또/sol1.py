# import sys
# sys.stdin = open("input.txt")
#
# T = 2
#
# for tc in range(1, T+1):


# 한줄에 있으므로 리스트로 받아옴
info = list(map(int, input().split()))
# 맨처음 k 와 나머지 리스트를 슬라이싱
k = info[0]
S = info[1:k+1]

# 결과값 초기화
result = []

# 부분집합 찾기
for i in range(1 << k):
    temp = []
    for j in range(k):
        if i & (1 << j):
            temp.append(S[j])
    # 부분집합 찾아진 것 중에서 원하는 길이가 6인것 탐색
    if len(temp) == 6:
        # 결과값에 추가
        result.append(temp)
# 숫자가 정렬될수 있도록 정렬
result.sort()
# 각각의 부분집합들을 원하는 모양대로 출력
for i in result:
    print(' '.join(map(str, i)))
# 공백을 위한 프린트
print()


# # 마지막 0 처리
# zero = input()