print('---------------')
print('# 2.5 변수와 함수')
print('## 2.5.1 변수')

print('### 제한 없는 정수형')

googol= 10 ** 100 # pow(10, 100)
print(type(googol))
print(googol)

print('\n---------------')
print('### dir() 함수')

s = 'string'
print(type(s))
print(dir(s)) # 객체가 갖고 있는 함수와 변수 리스트
print(s.__eq__('string'))
print(s.__contains__('ing'))

print('\n---------------')
print('### 예약어')
print(help('keywords'))




print('\n---------------')
print('## 2.5.2 함수')
print('### 연 평균 성장률 구하기')

def getCAGR(first, last, years):
    return (last/first)**(1/years) - 1

# 삼성전자 주가 : 1998.4.27 (65,300) -> 2018.4.27 (2,669,000)
cagr = getCAGR(65300, 2669000, 20)
print(cagr)
print("RESULT : {:.2%}".format(cagr))


print('\n---------------')
print('### None 반환값')
def func1():
    pass

def func2():
    return

def func3():
    return None

print(func1(), func2(), func3())
print(type(None))
print(func1() == None)
print(func1() is None)


print('\n---------------')
print('### None 반환값')

def myFunc():
    var1 = 'a'
    var2 = [1,2,3]
    var3 = max
    return var1, var2, var3 # 여러개 결과 값은 튜플 타입으로 반환된다

print(myFunc())

s, l, f = myFunc()
print(s)
print(l)
print(f)


print('\n---------------')
print('### lambda')

insertComma = lambda x : format(x, ',')
print(insertComma(1234567890))


print('\n---------------')
print('### 내장 함수 리스트')
# abs = 1
# print(abs(-100)) # abs는 내장함수(예약어)로 사용이 불가





print('\n---------------')
print('# 2.6 모듈과 패키지')
print('## 2.6.1 모듈')

print(help('modules')) # pc에 설치 된 모듈
print(help('modules time'))
print(help('time')) # 모듈 상세설명


print('\n---------------')
print('### import')
import keyword
print(keyword.kwlist) # module.kwlist : 해당 모듈의 예약어 확인


print('\n---------------')
print('### __file__ 속성')

print(keyword.__file__) # 임포트한 모듈의 위치


print('\n---------------')
print('### from ~ import ~')

import calendar
print(calendar.month(2020, 1))

from calendar import month
print(month(2020, 1)) # calendar 없이 바로 month로 호출 가능


print('\n---------------')
print('### import ~ as ~')

import datetime
print(datetime.datetime.now())

from datetime import datetime as dt
print(dt.now())




print('\n---------------')
print('## 2.6.2 패키지')

import urllib.request
print(type(urllib.request))



print('\n---------------')
print('### 패키지의 경로 속성')

import urllib
print(type(urllib))
print(urllib.__path__) # 패키지의 위치
print(urllib.__package__) # urllib가 속한 패키지



print('\n---------------')
print('### 패키지 생성하기')

import myPackage.moduleA
import myPackage.moduleB
print(myPackage.moduleA.functionA())
print(myPackage.moduleB.functionB())
# /workspace/study/python/myPackage/__pycache__


print('\n---------------')
print('### __init__.py 패키지 초기화 파일')

# /workspace/study/python/myPackage/__init__.py
from myPackage import *
print(moduleA.functionA())
print(moduleB.functionB())
print(moduleA.main()) # 실제 모듈명 반환


print('\n---------------')
print('### 파이썬의 선')

# 파이썬에 대한 철학...
import this
