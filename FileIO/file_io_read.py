
'''
* 파일 읽기 기능 (read)

- 파일로부터 데이터를 읽어들일 때는 분량에 따라 적당란 메서드 선택

1. read(): 파일 전체를 통째로 읽어서 리턴
2. readline(): 파일 데이터를 한 줄씩 읽어서 리턴
3. readlines(): 파일 전체를 읽어서 한 줄씩 분리한 후 리스트에 담아 리턴
'''
from os import close


file_path = 'D:/test/lunch.txt'

'''
try:
    f = open(file_path, 'r')
    text = f.read()
    print(text)
except:
    print('파일 로드 실패!')
finally:
    f.close()
'''

# readline(): 자동으로 \n을 기준으로 하여 데이터를
# 줄 단위로 읽어들이기 때문에 메모리 부담을 좀 더 줄일 수 있음

'''
try:
    f = open(file_path, 'r')
    while True:
        text = f.readline()
        if '국수' in text:
            print(text)
        if len(text) == 0:
            break
except:
    print('파일 로드 실패!')
finally:
    f.close()
'''

# readlines()는 파일 데이터를 한 줄씩 읽어서
# 리스트에 담아서 리턴하기 때문에 읽은 데이터를
# 리스트 문법을 사용해서 처리 가능

try:
    f = open(file_path, 'r')
    text = f.readlines() # text는 리스트
    #print(text)
    text.reverse()
    for t in text:
        print(t)
except:
    print('파일 로드 실패!')
finally:
    f.close()