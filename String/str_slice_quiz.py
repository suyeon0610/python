
ssn = input('주민등록번호를 입력하세요: ')

if int(ssn[:2]) < 21:
    year = int(ssn[:2]) + 2000
else:
    year = int(ssn[:2]) + 1900

if int(ssn[2:4]) < 10:
    month = ssn[3:4]
else:
    month = ssn[2:4]

if int(ssn[4:6]) < 10:
    day = ssn[5:6]
else:
    day = ssn[4:6]

age = 2021 - year + 1

if ssn[7] == 1 or ssn[7] == 3:
    sex = '남자'
else:
    sex = '여자'

print('주민등록번호 앞자리:' + ssn[:6])
print('주민등록번호 뒷자리:' + ssn[7:])
print(f'{year}년 {month}월 {day}일 {age}세 {sex}')