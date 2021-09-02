
'''
* points.txt 파일의 숫자값을 모두 읽어서 총합과 평균을 구한 뒤
총점, 평균값을 result.txt라는 파일에 쓰는 프로그램을 작성해 보세요.
'''
import traceback as trace # 예외 추적


try:
    file_path = 'D:/test/points.txt'
    
    f = open(file_path, 'r')
    nums = f.read().split()

except:
    print('파일 로드 실패!')
    print(trace.format_exc())
finally:
    f.close()

print(nums)
sum = 0
for n in nums:
    score = int(n)
    sum += score
    
avg = sum / len(nums)

try:
    file_path = 'D:/test/result.txt'
    f = open(file_path, 'w')

    data = f'총점: {sum}점, 평균: {avg:0.2f}점'
    f.write(data)
    print('파일 저장 완료')
except:
    print('파일 저장 실패')
    print(trace.format_exc())
finally:
    f.close()