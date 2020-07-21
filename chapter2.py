import os

print('---------------')
print('# 2.3 문자열과 산술연산')
print('## 2.3.1 문자열')

name = 'woonji'
print('hello ' + name + '\'s word')
print(os.getenv)

print(type('Hello, world!'))

print('\n---------------')
print('### escape 문자 처리')

print('C:\Windows\System32\notepad.exe')
print(r'C:\Windows\System32\notepad.exe')

print('\n---------------')
print('### 작은 따옴표와 큰 따옴표')

print('\"It\'s not that I\'m so smart; it\'s just that I stay with problems longer.\" Albert Einstein')

print('\n---------------')
print('### 여러 줄 입력하기')

print('''Wake up, Neo...'
The Matrix has you...
Follow the white rabbit''')

print('\n---------------')

# 한 줄 주석
'''
주석
여러줄
'''
"""
주석
여러줄
"""

print('### 인덱싱')
word = 'Python'
print(len(word))
print(word[0] + word[1] + word[2] + word[3] + word[4] + word[5])
# 첫 문자 : -n, 마지막 문자 : -1
print(word[-6] + word[-5] + word[-4] + word[-3] + word[-2] + word[-1])

print('\n---------------')
print('### 슬라이싱')

print(word[0:6])
print(word[0:])
print(word[:6]) # 5번째 인덱스에 해당하는 문자까지




print('\n---------------')
print('## 2.3.2 산술 연산')

print(1+2)
print(3-4)
print(5*6)
print(2**8) # 2의 8승. equal pow(2, 8)
print(pow(2,8))
print(5/3)
print(5//3) # 나눗셈 결과의 몫
print(5%3) # 나눗셈 결과의 나머지

x = 2
x += 1
print(x)
print('x : ', x)




print('\n---------------')
print('## 2.3.3 흐름제어')

rsi = 88 # 상대강도지수
if rsi > 70: # 과매수
    print('RSI', rsi, 'means overbought.')
elif rsi < 30: # 과매도
    print('RSI', rsi, 'means oversold.')
else:
    print('...')

print('\n---------------')
print('### for 반복문')

for i in [1,3,5]:
    print(i)

print('\n---------------')
print('### range 반복문')

for i in range(1, 7, 2): # 시작값, 멈춤값, 증가값
    print(i)

print('\n---------------')
print('### enumerate 반복문')

INTERNET = ['google', 'naver', 'daum', 'yahoo']
for idx, symbol in enumerate(INTERNET, 1): #반복 자료형, 인덱스 시작값
    print(idx, symbol)

print('\n---------------')
print('### while 반복문')

i = 1
while i < 7:
    print(i)
    i+=2

print('\n---------------')
print('### while else와 for else')

i = 0
while i >= 0:
    i += 1
    if (i % 2) == 0:
        continue
    if i > 5:
        break
    print(i)
else:
    print('Condition is False')

print('\n---------------')
print('### try except 예외처리')

try:
    1/0
except Exception as e:
    print('Exception occured : ', str(e))






print('\n---------------')
print('# 2.4 반복 자료형')
print('## 2.4.1 리스트')

ls = ['one', 'two', 'three', 4, 5, 6]

print([ls[0], ls[-1]])

L = [[1,2], [3,4]]

print(L[0], L[1])

print(L[0][0], L[0][1], L[1][0], L[1][1])

print(L*3)

print('\n---------------')
print('### split() 함수')

myList = 'Thoughts become things.'.split()
print(type(myList))
print(myList)

print('\n---------------')
print('### join() 함수')

print(' '.join(myList))

print('\n---------------')
print('### sort()와 sorted()')

li = [2,5,3,1,4]
li.sort()
print(li)
li2 = [4,3,1,2,5]
li3 = sorted(li2)
print(li2)
print(li3)

print('\n---------------')
print('### append()와 extend()')

L = [1,2]
L.append([3,4])
print(L)
L2 = [1,2]
L2.extend([3,4])
print(L2)

print('\n---------------')
print('### 구분자 변경하기')

print('-'.join('2020/07/21'.split('/')))
print('2020/07/22'.replace('/', '-'))

print('\n---------------')
print('### 천 단위 숫자를 쉼표로 구분하기')

print(''.join('1,234,567,890'.split(',')))
print('1,234,567,890'.split(','))
print('1,234,567,890'.replace(',', ''))
print(format(1234567890, ','))


print('\n---------------')
print('### 리스트 복사')

myList = ['Thoughts', 'become', 'things.']
newList = myList[:] # 전체 영역 슬라이싱 [:]하여 새로운 리스트 반환
print(newList)
newList[-1] = 'actions.'
print(newList)
print(myList)


print('\n---------------')
print('### 리스트 내포')

nums = [1,2,3,4,5]
squres = []
for x in nums:
    squres.append(x ** 2)
print(squres)
print([x ** 2 for x in nums]) # 요게 리스트 내포..
print([x ** 2 for x in nums if x % 2 == 0])




print('\n---------------')
print('## 2.4.2 변경이 불가능한 튜플')

myTuple = ('a', 'b', 'c', [10,20,30], abs, max)
print(myTuple[3])
print(myTuple[4](-100)) # 5번째 원소인 내장함수 abs(절대값 구하는 함수)에 -100을 파라미터로 전달
print(myTuple[5](myTuple[3])) # 6번째 원소인 내장함수 max(최대값 구하는 함수)에 리스트를 파라미터로 전달

# 튜플 객체는 원소 할당을 지원하지 않는다. (리스트와의 차이점..)
# myTuple[0] = 'A'




print('\n---------------')
print('## 2.4.3 {키:값} 형태 딕셔너리')

fruit = {'BANANA' : 'yello', 'STRAWBERRY' : 'red'}
# print(fruit[1]) # 순서가 없으므로 인덱스 숫자로 접근할 수 없다.
print(fruit['STRAWBERRY'])
fruit['WATERMELON'] = 'green' # 딕셔너리에 원소 추가 시 키:값을 지정해주어야 함
print(fruit)
print(len(fruit))




print('\n---------------')
print('## 2.4.4 문자열 포맷 출력')
print('### % 기호방식')

for x in fruit:
    print('%s : %s' % (x, fruit[x])) # %기호를 사용하여 문자 출력 형식 지정

print('### {} 기호방식')

for x in fruit:
    print('{} : {}'.format(x, fruit[x]))

print('### f-strings 방식')

for x in fruit:
    print(f'{x} : {fruit[x]}') # f가 format을 의미하는듯...





print('\n---------------')
print('## 2.4.5 중복 없는 셋')

s = {'A', 'P', 'P', 'L', 'E'}
print(s)
mySet = {'B', 6, 1, 2}
print(mySet) # 순서 보장되지 않음
if 'B' in mySet:
    print("'B' exists in", mySet)

setA = {1,2,3,4,5}
setB = {3,4,5,6,7}

print(setA & setB) # 교집합
print(setA.intersection(setB))
print(setA | setB) # 합집합
print(setA.union(setB))
print(setA - setB) # 차집합
print(setA.difference(setB))
print(setB - setA) # 차집합
print(setB.difference(setA))

ls = [1,3,5,2,2,3,4,2,1,1,1,5]
print(list(set(ls))) # 셋을 이용하여 쉽게 중복 제거





print('\n---------------')
print('## 2.4.6 타임잇으로 성능 측정하기')

import timeit

# 10000개의 원소를 순회하는 동작을 1000 번 반복하는데 걸린 시간 비교
iteration_test = """
for i in itr :
    pass
"""

print('list : ', timeit.timeit(iteration_test, setup='itr = list(range(10000))', number=1000)) # 측정하고자 하는 코드, 측정 시 사용할 원소, 반복 횟수
print('tuple : ', timeit.timeit(iteration_test, setup='itr = tuple(range(10000))', number=1000))
print('set : ', timeit.timeit(iteration_test, setup='itr = set(range(10000))', number=1000))

print('\n---------------')

search_test = """
import random
x = random.randint(0, len(itr)-1)
if x in itr :
    pass
"""

print('list : ', timeit.timeit(search_test, setup='itr = list(range(10000))', number=1000)) # 측정하고자 하는 코드, 측정 시 사용할 원소, 반복 횟수
print('tuple : ', timeit.timeit(search_test, setup='itr = tuple(range(10000))', number=1000))
print('set : ', timeit.timeit(search_test, setup='itr = set(range(10000))', number=1000))