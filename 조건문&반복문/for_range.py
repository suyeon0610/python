
'''
* 내장함수 range()

- 순차적으로 증가하는 정수의 순차적 자료형을 만들 때
 대괄호 안에 데이터들을 콤마로 일일히 나열하는 것은 한계가
 있기 때문에, range함수를 사용하여 보다 쉽게 순차형 반복 범위 생성

 ex) range(begin, end, step)
  begin은 값이 포함되지만(이상), end는 값이 포함되지 않음(미만)
'''

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

list2 = list(range(1, 11, 1))
print(list2)

# step 생략 시 자동으로 1로 처리
list3 = list(range(4, 15))
print(list3)

# range함수 괄호 안에 값을 한 개만 주면 end로 처리하고
# begin값을 자동으로 0으로 처리
list4 = list(range(5)) # range(0, 5, 1)

print('-' * 40)

# 1~100까지의 누적합
total = 0
for n in range(1, 101):
    total += n
print(total)

'''
- 정수 하나 입력받아서 1부터 해당 수까지의 모든 소수 & 소수 개수 출력
'''

nums = []
num = int(input('정수를 입력하세요: '))

for n in range(1, num+1):
    count = 0
    for m in range(1, n+1):
        if n % m == 0:
            count += 1

    if count == 2:
        nums.append(n)

print('*** 소수 구하기 ***')
print('입력값:', num)
print('소수:', nums)
print('개수: ', len(nums),'개')
            