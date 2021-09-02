
'''
* 표준 모듈 time

- time모듈: 시간관련 기능들 제공

- time() 함수: 현재 시간을 1970년 1월 1일 자정을
 기준으로 현재까지 경과한 시간을 초 단위로 표현한 유닉스 시간 반환
'''
import time
print(time.time())

# time 함수를 이용한 프로그램 속도 측정 테스트

start = time.time()

sum = 0
for n in range(500000):
    sum += n 

end = time.time()

print(f'프로그램 실행 속도: {end-start:0.4f}초')

'''
- sleep() 함수: cpu를 지정한 시간만큼 잠재워 아무것도 하지 않고 시간을 끔
'''

print('재밌는 문제 준비했어용')
time.sleep(3)
print('대학생이 힘이 쎈 이유는?')
time.sleep(15)
print('개강하니까~')