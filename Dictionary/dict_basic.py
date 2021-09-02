
'''
* 사전 (Dictionary)

- 사전은 키(key)와 값(value)의 쌍을 저장하는 대용량의 자료구조
- 사전은 Map이라고도 부르며 연관배열이라고도 부름
- 사전을 정의하는 기호는 {}이고, 괄호안에 데이터를
 key:value 형태로 나열하여 저장
'''

students = {'멍멍이':'김철수', '야옹이':'박영희', '짹짹이':'홍길동'}
print(type(students))
print(len(students))

'''
- 사전에 사용도는 key값은 중복값을 가질 수 없고 변경도 안됨
- 그러나 value값은 중복을 허용하며 데이터를 자유롭게 편집 가능
- 사전 내부에 저장된 데이터를 검색할 때는 인덱스 대신 key 사용 (시퀀스 자료 x)
'''
print(students['멍멍이'])
# print(students['메롱'])

# in 키워드를 사용하여 key의 존재 유무 확인 가능
print('멍멍이' in students)
print('메롱' in students)

'''
* 코딩도장 연습문제
다음 소스 코드를 완성하여 게임 캐릭터의 체력(health)과 이동 속도(movement speed)가 출력
'''
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}
 
print(camille['health'])
print(camille['movement_speed'])

'''
* 코딩도장 퀴즈
표준 입력으로 문자열 여러 개와 숫자(실수) 여러 개가 두 줄로 입력됩니다. 
입력된 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성한 뒤 
딕셔너리를 출력하는 프로그램을 만드세요. input().split()의 결과를 변수 한 개에 저장하면 리스트로 저장됩니다.
'''
key = input().split()
value = list(map(float, input().split()))
tu = dict(zip(key, value))
print(tu)