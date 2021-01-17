# API 요청 & 응답
# nationalize.io

# 1. 요청에 필요한 기능 묶음(라이브러리)을 가져온다. (import)
import requests, pprint

# 2. API 요청 URL 확인한다. (+ 필요한 데이터 넘겨주기)
name = 'ruby'
url = f'https://api.nationalize.io/?name={name}'

# 3. 요청 보낸다.
response = requests.get(url).json()
pprint.pprint(response)

# 4. 응답 결과 확인 후 정보 추출하기
name = response['name']
country_id = response['country'][0]['country_id']
probability = round(response['country'][0]['probability'] * 100, 2)

# 최종 결과값 출력
# ___의 국적은 ___% 확률로 __입니다.
print(f'{name}의 국적은 {probability}% 확률로 {country_id}입니다.')
