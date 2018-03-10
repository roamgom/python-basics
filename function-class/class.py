# 보통 함수 사용시
result = 0

def add(num):
    global result
    result += num
    return result

print(add(3), end=' ')
print(add(4))
# 3 7

# 여러 계산 결과를 위한 함수
result1 = 0
result2 = 0

def adder1(num):
    global result1
    result1 += num
    return result1

def adder2(num):
    global result2
    result2 += num
    return result2

print(adder1(3), end=' ')
print(adder1(4))
print(adder2(3), end=' ')
print(adder2(7))
# 3 7
# 3 10


# 클래스 사용
class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3), end=' ')
print(cal1.adder(4))
print(cal2.adder(3), end=' ')
print(cal2.adder(7))
# 3 7
# 3 10

# 계산기 예제
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)
print(a.sum(), end=' ')
print(a.sub(), end=' ')
print(a.mul(), end=' ')
print(a.div())

print(b.sum(), end=' ')
print(b.sub(), end=' ')
print(b.mul(), end=' ')
print(b.div())

# 6 8 2 2
# 10 21 -4 0

# 클래스 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.sum(), end=' ')
print(a.pow())
# 6 16

# 메소드 오버라이딩
class OneMoreFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result
a = OneMoreFourCal(4, 0)
a.div()
# 0
