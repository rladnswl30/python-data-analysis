print('\n---------------')
print('# 2.7 객체지향 프로그래밍')
print('## 2.7.1 클래스')
class MyFirstClass:
    clsVar = 'The best way to predict the future is invent it'
    def clsMethod(self):
        print(MyFirstClass.clsVar + '\t- Alan Curtis Kay -')

mfc = MyFirstClass() # 인스턴스화
print(mfc.clsVar) # 클래스 변수에 접근
print(mfc.clsMethod()) # 클래스 메서드 호출

print('\n---------------')
print('## 2.7.2 상속')
class A:
    def methodA(self):
        print("Calling A's methodA")
    def method(self):
        print("Calling A's method")

class B:
    def methodB(self):
        print("Calling B's methodB")

class C(A, B): # C 는 자식 클래스, A, B 부모 상속
    def methodC(self):
        print("Calling C's methodC")
    def method(self):
        print("Calling C's overriden method")
        super().method()

c = C()
c.methodA()
c.methodB()
c.methodC()
c.method()

print('\n---------------')
print('## 2.7.4 클래스 메서드')

class NasdaqStock:
    """Class for NASDAC stocks"""
    count = 0 # 클래스 변수
    def __init__(self, symbol, price):  # 생성자 (인스턴스 생성 시 자동으로 호출된다)
        """Constructor for NasdaqStock"""
        self.symbol = symbol # 인스턴스 변수
        self.price = price # 인스턴스 변수
        NasdaqStock.count += 1
        print('Calling __init__({}, {:.2f}) > count : {}'.format(self.symbol, self.price, NasdaqStock.count))
    def __del__(self): # 소멸자
        """Destructor for NasdaqStock"""
        print('Calling __del__({})'.format(self))

gg = NasdaqStock('GOOG', 1154.05)
del(gg)
ms = NasdaqStock('MSFT', 102.44)
del(ms)
amz = NasdaqStock('AMZN', 1746.00)
del(amz)


print('\n---------------')
print('### __doc__ 독스트링')
help(NasdaqStock)