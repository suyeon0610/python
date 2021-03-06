'''
* 리스트의 내부 요소 다루기

- 리스트는 시퀀스 자료형이기 때문에 인덱스를 통한 요소들의 관리 가능
- 리스트를 다룰 때는 문자열과 비슷한 방식 사용
'''

pokemon = ['피카츄', '라이츄', '파이리', '꼬부기', '버터풀']

print(pokemon[2])
print(pokemon[1][2])
print(pokemon[4][:2])

# 리스트 슬라이싱 -> 리스트데이터[brgin:end:step]
nums = [0,1,2,3,4,5,6,7,8,9]

print(nums[2:5:1])
print(nums[:4])
print(nums[1:7:2])

print('-' * 40)
print(nums)

nums[2] = 34
print(nums)

nums[7] = 88
print(nums)

nums[3] = nums[6]
print(nums)

'''
- 문자열은 상수 형태로 저장되는 고정형 리스트임
- 따라서 인덱싱이나, 슬라이싱을 통해 값의 복사본을 활용하는 것은 가능하지만,
 영역에 직접 접근하여 내부의 값을 편집할 수 없음
- 문자열은 변경이 불가능한 자료형임. (immutable)
'''

s = 'python'
# s[2] = 'x' (x)

# umpackaging: 리스트 내부 요소를 다시 변수에 저장
# pokemon = ['피카츄', '라이츄', '파이리', '꼬부기', '버터풀']
'''
p = pokemon[0]
r = pokemon[1]
c = pokemon[2]
s = pokemon[3]
b = pokemon[4]
'''

# 좌항의 변수의 개수와 우항의 리스트의 요소의 개수가 일치한다면
# 자동으로 변수에 리스트 내부 요소의 값이 저장 됨
p,r,c,s,b = pokemon
print(p,r,c,s,b)

# 빈 리스트 만들기
list1 = []
list2 = list()

'''
* 코딩도장 연습문제
리스트 [5, 3, 1, -1, -3, -5, -7, -9] (range 이용)
'''
a = list(range(5, -10, -2))
print(a)
