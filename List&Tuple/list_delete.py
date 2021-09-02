
'''
* 리스트 내부 요소 삭제

1. remove(): 삭제할 값을 직접 지정하여 삭제
2. 내장함수 del(): 삭제할 요소의 인덱스를 통해 삭제
3. clear(): 리스트 내부 요소 전체 삭제
'''

points = [88, 99, 56 ,92, 100, 78]

points.remove(92)
print(points)

del(points[2])
print(points)

'''
- 삭제할 이름을 입력받아서 해당하는 이름을 실제로 리스트에서 삭제 후
 정보를 출력 (리스트 출력)

- remove()와 del()을 이용하려 각각 출력
'''
pokemon = ['피카츄', '라이츄', '파이리', '꼬부기', '버터풀']

p = input('삭제할 포켓몬을 입력하세요: ')

i = 0

# remove
if p in pokemon:
    pokemon.remove(p)
else:
    print()

# del1
while True:
    if pokemon[i] == p:
        del(pokemon[i])
        break
    else:
        i += 1
    
    if i == len(pokemon):
       print('존재하지않는 포켓몬입니다.') 
       break

# del2
for idx in range(5):
    if p == pokemon[idx]:
        del(pokemon[idx])
        break
print('삭제 후 정보: ', pokemon)