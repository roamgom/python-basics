# 함수의 기본적인 형태
def 함수명(인수):
    <수행문장>
    return 값

# 일반적인 함수(입력값, 리턴값)
def sum(a,b):
    result = a + b
    return result
# 함수 호출
a = 3
b = 4
c = sum(a,b)
print(c)
# 7

# 입력값만 있는 함수
def sum(a, b):
    print(f"{a} + {b} = {a+b}")
    # print(a," + ",b,)

# 리턴값만 있는 함수
def hello():
    return 'Hi'

# 입력값, 리턴값 둘 다 없는 함수
def hello():
    print('Hello')


# 입력값이 여러개인(몇 개일지 짐작이 안되는) 경우
def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


# 리턴값은 하나다
def sum_and_mul(a,b):
    return a+b, a*b

# 위의 함수는 튜플 형태로 반환한다.
# 위의 함수를 실행하기 위해서는 아래와 같이 실행해야 한다.
sum, mul = sum_and_mul(3, 5)


# 리턴은 다른 용도로 쓰일 수 있다.
def yes_quiz(word):
    if word == "yes":
        print("yes라고 대답하셨습니다.")
        return
    print(f"yes가 아닌 {word}라고 대답하셨습니다.")


# 초기값 인자
def man_or_woman(name,old,man=True):
    print(f"나의 이름은 {name}")
    print(f"나이는 {old}")

    if man:
        print("남자")
    else:
        print("여자")

man_or_woman("홍길동",24,True)


# 잘못 설정할 경우
def man_or_woman(name,man=True,old):
    print(f"나의 이름은 {name}")
    print(f"나이는 {old}")

    if man:
        print("남자")
    else:
        print("여자")

man_or_woman("홍길동",True,24)


# 함수 안과 밖의 변수 효력 범위
a = 1
def number(a):
    a = a + 1

number(a)
print(a)


# 변수 안의 내용 적용 방법
# 1. return 사용
a = 1
def number(a):
    a = a + 1
    return a

a = number(a)
print(a)

# 2. global 변수 적용
a = 1
def number():
    global a
    a = a + 1

number(a)
print(a)

# 3. return 사용
a = 1
def number(a):
    a = a + 1
    return a

a = number(a)
print(a)

# 오류의 경우
def number(a):
    a = a + 1

number(3)
print(a)