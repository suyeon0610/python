
'''
* 집합(set) 메서드

- 집합은 사전(dictionary)과 마찬가지로 {}로 표현하지만, key:value 쌍이 아닌
 데이터가 하나씩 들어간다는 점이 다름

- set()함수는 공집합을 만들기도 하며, 다른 컬렉션 자료를
  집합 형태로 변환 할 수 있음
'''

# []-list(), tuple(), {}-dict(), set()

names = {'홍길동', '김철수', '박영희', '고길동', '홍길동'}
print(type(names))
print(names)

for x in names:
    if x == '박영희':
        print(x)
        break

# 내장 함수 set()
s = set()
print(type(s))
print(s)

s1 = 'programming'
print(set(s1))
print(list(s1))
print(tuple(s1))

'''
- 집합은 변경 가능한 자료형이어서 언제든지 데이터 편집 가능 

- 집합에 요소를 추가할 때는 add() 메서드 사용,
 제거할 때는 remove()사용
'''

print('-' * 40)

asia = {'korea', 'china', 'japan'}
print(asia)

asia.add('thailand')
asia.add('china')
asia.remove('japan')
print(asia)

# 집합의 결합은 update() 메서드 사용 (덧셈 연산 x)
asia2 = {'singapore', 'indonesia', 'korea'}
# print(asia + asia2) (x)
asia.update(asia2)
print(asia)
