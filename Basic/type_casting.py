
name = '홍길동'
score = 90

'''
- 문자열과 정수의 + 연산 진행 시 타입이 일치하지 않아서
 에러가 발생하므로, 타입을 어느 한 쪽으로 맞춰야 함

- 정수나 실수를 문자열로 변환할 때는 str() 내장 함수를 사용
'''

print(name + '의 점수는 ' + str(score) + '입니다.')

# 숫자로 이루어진 문자열을 정수로 변환할 때는 int()를 사용
n1 = 10
n2 = '34'
print(n1 + int(n2))

# 반올림을 할 때는 round() 함수 사용
print('-' * 40)

print(round(4.78))

print(round(4.78, 1))