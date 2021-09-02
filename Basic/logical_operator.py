
'''
* 논리 연산자 (&, |, and, or, not)

# &, and: 좌항과 우항의 논리값이 모두 True일 경우에만 전체 결과 True 도출
'''
a = 5

if a > 1 and a < 10:
    print('asms 1~10 사이의 숫자가 아닙니다.')
else:
    print('a는 1~10 사이의 숫자가 아닙니다.')

# 파이썬은 위의 식을 연결해서 작성 가능
if 1 < a < 10:
    print('ok!')

'''
|, or: 좌항과 우항의 논리값이 한 쪽만 True여도 전체 결과 True 도출
'''

'''
* 단축 평가 여산 (short circuit: and, or)
- 좌항에서 전체 결과가 판명났을 경우 우항 연산을 진행하지 않는 연산자
'''

c = 0

if(c == 0) or (10 / c == 5): # 우항에서 100% 에러가 나는 상황
    print('에러 없이 통과')

# not 여산자는 논리값을 반전시킴

'''
- c언어에서는 정수 0을 False로 해석하고, 
0이 아닌 모든 정수를 True로 해석 (논리형 없음)
파이썬에서도 C의 논리해석 그대로 적용 가능
'''

apple = 5
if not apple:
    print('사과가 하나도 없습니다.')
else:
    print('사과가', apple, '개 있습니다.')

'''
* 코딩도장 연습문제
국어, 영어, 수학, 과학 점수가 있을 때 한 과목이라도 50점 미만이면 불합격,
 다음 소스 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되게 만드세요.
'''
korean = 92
english = 47
mathematics = 86
science = 81

if korean >= 50 and english >= 50 and mathematics >= 50 and science >= 50:
    print('합격')
else:
    print('불합격') 

'''
* 코딩도장 퀴즈
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 국어는 90점 이상, 
영어는 80점 초과, 수학은 85점 초과, 과학은 80점 이상일 때 합격이라고 정했습니다
(한 과목이라도 조건에 만족하지 않으면 불합격). 
다음 소스 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되게 만드세요
'''
kor, eng, math, sc = map(int, input().split())
print( kor >= 90 and eng > 80 and math > 85 and sc >= 80)
