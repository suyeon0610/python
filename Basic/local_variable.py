
'''
* 지역 변수 (local variable)

- 지역 변수란 함수 내부에 선언된 변수

- 지역변수는 함수 내부에서만 사용할 수 있으며 함수의 호출이 종료되는 순간
 메모리에서 자동 소멸 됨

- 지역변수의 사용을 함수 내부로 제한하는 이류는 변수의 이름 충돌을
 피하고 메모리를 절약하기 위함 임
'''

def info():
    name = '안녕'
    print(name)

info()
# print(name) (x)
