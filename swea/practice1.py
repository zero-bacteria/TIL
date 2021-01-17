# # x% 농도의 소금물 y g과 물 z g 을 혼합한 소금물의 농도를 소수점 두번째 까지

# x= int(input("소금물의 농도(%)를 입력하세요 : "))
# y= int(input("소금물의 양(g)을 입력하세요 : "))
# z= int(input("혼합할 물의 양(g)을 입력하세요 : "))

# result = ((y*x*0.01)/(y+z))*100

# print ("혼합된 소금물의 농도: %0.2f%% "%result)


# 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하시오

# a= int(input())
# count = 0

# for i in range(1,a+1):
#     if not a%i:
#         print('%d(은)는 %d의 약수입니다.'%(i,a))
#         count+=1
#         if count ==2:
#             print('%d(은)는 1과 %d로만 나눌수 있는 소수 입니다.'%(a,a))


# 대문자 소문자 아스키 


# islower은 소문자인지 아닌지 맞으면 정수 반환 틀리면 0 // ord()는 아스키 코드로 나타내 주는것 

# a=input()
# if a.islower():
#    print("%s(ASCII: %d) => %s(ASCII: %d)" % (a, ord(a), a.upper(), ord(a.upper())))
# elif a.isupper():
#    print("%s(ASCII: %d) => %s(ASCII: %d)" % (a, ord(a), a.lower(), ord(a.lower())))
# else :
#    print(a)



