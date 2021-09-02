
import random

rn = random.randint(1, 100)
# print(rn)
opt = 5

print('*** UP & DOWN ***')
while True:
    if opt != 0:
        num = int(input(f'숫자를 입력해주세요 (기회:{opt}): '))
        if num > rn:
            print('DOWN!!')
            opt -= 1
        elif num < rn:
            print('UP!!')
            opt -= 1
        else:
            print(f'정답 입니다~!! (정답: {rn})')
            break
    else:
        print('기회를 모두 사용하셨습니다~ㅠㅠ')
        print('정답:', rn)
        break
