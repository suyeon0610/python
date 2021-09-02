'''
* 표준 입력함수 input()

- 함수 괄호 한에 사용자에게 질문할 내용을 문자열 형태로 작성

- input()과 함께 변수를 선언해서 입력값을 받아주어야 함
입력받은 데이터의 타입은 str로 저장 됨
'''
nick = input('별명이 뭐야?')
print('내 별명은 ' + nick + '입니다.')

# 입력값이 정수, 실수라면 input함수 자체를 int(), float() 함수로 감싸줌
# input함수의 리턴값이 문자열이기 때문에 변환함수로 변환 함

price = int(input('음식 가격: '))
people = int(input('사람 수: '))

print('지불할 가격: ', price*people, "원")

'''
* 값 여러개 한번에 입력하기

1. a, b = input('숫자 두개 입력:').split('기준문자열')
- split의 결과를 정수로 변환해 주어야 함

2. a, b = map(int, input('숫자 두개 입력:').split('기준문자열'))
'''