
# * 표준 출력 함수 print()
# ()안에 출력하고 싶은 변수, 리터럴 상수, 수식 등을 적음
# 터미널에 텍스트 출력 실행

'''
- 출력할 데이터가 여러 개라면 괄호 안에 출력할 데이터들을
 콤마로 나열해서 작성 함
'''

cat = '야옹이'
dog = '멍멍이'
print(cat, dog)

'''
- print함수 내부에는 sep라는 속성이 존재
- sep은 seperator의 약자로 구분자라고도 함
 만약 변경을 원한다면 sep속성을 직접 작성하여 변경함
'''

print('-------------------------------')
# print(cat, dog, '좋아요', sep=' ') -> 기본값
print(cat, dog, '좋아요', sep='')
print(cat, dog, '좋아요', sep='♥')

'''
- end: 데이터 출력 이후 맨 끝에 포함할 문자 지정

- 기본값: \n 이므로 print함수 사용 시 자동으로 줄 개행이 되는것 처럼 보임
'''

#print(cat, dog, '좋아요', end='\n')
print(cat, dog, '좋아요', end=' ')
print('이 문장은 줄 개행이 될까')

print(cat, dog, '좋아요', sep='~', end=' ')
# 출력할 내용이 먼저 전달되어야 함
# print(sep='~', end=' ', cat, dog, '좋아요')

