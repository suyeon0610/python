
'''
* 문자열 분할

- split()메서드는 구분자를 기준으로 문자열을 분할하여 리스트로 담아 반환
'''
s1 = '떡볶이 김말이 닭강정'
print(s1.split()) # 괄호 안을 비우면 공백을 구분자로 하여 분할

s2 = '홍길동 | 대한출판사 | 2021년 8월'
data = s2.split('|')
print(data)
print('저자:' + data[0])
print('출판사:' + data[1])
print('출판일:' + data[2])
