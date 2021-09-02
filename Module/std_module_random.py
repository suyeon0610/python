
'''
* 표준 모듈 random

- 프로그램이 무작위 동작을 하게 하려면 난수값(랜덤값)이 필요함

- random 모듈: 랜덤값을 난수라도 부르며, 난수를 쉽게 
 발생 시킬 수 있는 함수를 제공하는 모듈

- random 모듈의 random() 함수는 0.0이상 1.0미만의 실수 난수 값 발생
'''

import random as r

rn = r.random()
# print('랜덤값:',rn)

'''
- randint(): 정수 난수
- 인수로 시작범위와 끝 범위 지정, 끝 범위도 난수값에 포함됨 (이하) 
'''
pets = ['멍멍이', '야옹이', '짹짹이', '호랑이', '코끼리']
idx = r.randint(0, 4) # 0이상 4이하
print('나의 반려동물은? ', pets[idx])

# choice(): 리스트 내부의 임의의 요소를 랜덤으로 선택하여 리턴
print('나의 반려동물은? ', r.choice(pets))

# shuffle(): 리스트의 요소를 무작위로 섞음
print(pets)
r.shuffle(pets)
print(pets)

# sample(): 리스트의 항목 중 n개를 무작위로 추출하여 새로운 리스트 만듦
# 중복값은 자동으로 배제시키며, 원본 리스트는 변하지 않음

print('-' * 40)
s_list = r.sample(pets, 2)
print(s_list)
print(pets)

# sample함수를 활용한 로또번호 6개 뽑기(중복 알아서 제거)
lotto_nums = list(range(1, 46))
lotto = r.sample(lotto_nums, 6)
lotto.sort()
print(lotto)