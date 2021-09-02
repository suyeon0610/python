
'''
* 반복문 (loop)

- 반복문은 유사한 명령을 반복해서 실행하는 제어문
- 파이썬의 반복문: while, for ~ in
'''

# while문에 필요한 3요소: 제어변수(begin), 조건식(end), 증감식(step)

i = 1
total = 0
while i <= 10:
    total += i
    i += 1 # 파이썬은 증감 연산자 없음 (++, --)

print('1부터 10까지의 누적합: ', total)

x = int(input('x값을 입려하세요: '))
y = int(input('y값을 입력하세요: '))
temp = 0

i = x
total = 0

'''
if x > y:
    temp = x
    x = y
    y = temp
'''

if x > y:
    x, y = y, x

while x <= y:
    total += x

print('x부터 y까지의 누적합계:', total)