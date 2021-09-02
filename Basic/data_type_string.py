
'''
* 문자열(string)
- 단일 문자들을 따옴표로 감싸서 나열한 문자 데이터의 집합형태
- 따옴표 안에 어떤 형태의 데이터가 들어가도 문자로 인식
- 전 세계의 모든 문자를 저장할 수 있고, 길이에도 제한 없음
'''
# 탈출문자를 적용해서 (\) 따옴표를 문자로 표현
s1 = "나는 그에게 \"도와줘!\"라고 말했다."

file1 = 'c:\\temp\\new.jsp'

# 문자열 앞에 r이라는 접두어를 붙이면
# 해당 문자열 탈출 문자를 적용하지 않음
file2 = r'c:\temp\new.jpg'
print(file2)

# 한 줄로 쓰기에 너무 긴 문자열을 문단으로 처리하는 방법
# 파이썬은 문장 주석 없음 -> 변수에 대입하지 않은 문자열을 문자 주석처럼 사용
anthem = '''
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼처리 화려강산
대한사람 대한으로 길이 보전하세
'''
print(anthem)

# \를 문장 끝에 붙여주면 line continue 효과
anthem2 = '''
동해물과 백두산이 마르고 닳도록\
하느님이 보우하사 우리나라 만세\
무궁화 삼처리 화려강산\
대한사람 대한으로 길이 보전하세
'''
print(anthem2)

'''
* 문자열 연산

- 파이썬은 문자열의 덧셈 연산과 곱셈 연산을 지원함
- 덧셈 연산시 문자열을 서로 연결하여 결합 함
- *로 문자열을 정해진 수 만큼 반복 연결 함
'''

print('배고파' * 4)