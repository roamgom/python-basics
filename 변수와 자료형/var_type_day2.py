'''
문자열 자료형

하나의 문자, 혹은 여러개의 문자가 결합된 문자열을 포함

문자열은 4개의 표현 방식이 존재
1. '' 작은 따옴표
2. "" 큰 따옴표
3. ''' ''' 작은 따옴표 3개를 이용하여 둘러싸기
4. """ """ 큰 따옴표 3개를 이용하여 둘러싸기

'''

sentence = 'my name is eddie'
sentence = "my name is eddie"

#따옴표를 중복 시키고 싶은 경우는 \(백슬래시)를 붙혀 사용
sentence = 'it\'s a beautiful day'
sentence = "he said \"hello\" to me"

#여러 줄을 입력하고 싶으면 \n을 사용
sentence = 'my\n name\n is\n eddie'
sentence = "my\n name\n is\n eddie"

#혹은 3개를 겹쳐 쓰자
sentence = '''my
name
is
eddie'''
sentence = """my
name
is
eddie"""

'''
문자열 더하기

문자열은 + 기호를 사용하여 서로 붙힐 수 있고,
         * 기호를 써서 여러번 출력하는것도 가능하다
'''

head = 'hello'
tail = 'world'
head + tail
tail + head
head * 2

'''
콘솔 창에 문자열을 출력 하기 위해서 
print() 함수를 이용한다

'''

#print 사용 예
print('my name is eddie')

print('=' * 20)
print('program start')
print('=' * 20)

'''
문자열 슬라이싱

문자열은 순서를 갖는다
hello 와 같은 문자열이 있을때 
h = 0번째 <---> -5번째
e = 1번째 <---> -4번째
l = 2번째 <---> -3번째
l = 3번째 <---> -2번째
o = 4번째 <---> -1번째
와 같이 순서는 항상 0번 부터 시작하고,
뒤에서 부터 셀 때는 -1부터 시작한다
'''

a = 'hello'
print(a[2])
print(a[-2])

'''
: 을 이용하여 슬라이싱

a[시작 번호:끝 번호] 를 이용하여 슬라이싱 가능
a[0:3] 으로 슬라이싱 하면
0 <= a < 3 의 범위로 슬라이싱됨

a[시작 번호:] 인 경우 시작 부터 마지막까지
a[:끝 번호] 인 경우 처음부터 끝 번호 까지
'''

a = 'hello world'
print(a[0:5])
print(a[5:])
print(a[:5])

'''
포맷팅

문자열 내에 값을 삽입하는것
예를 들어 오늘의 날짜를 출력하는 경우
매일 날짜가 변하는데 이를 전부 다른 문자열로 하는것은 비효율적
따라서 포맷팅을 사용하는 것이 편리
'''

#변수 day에 요일만 바꿔주면 된다
day = 'monday'
string = f"today is {day}"
print(string)

#여러개의 변수를 대입하는 방법

month = 3
day = 5
string = f"오늘은 {month}월 {day}일 입니다"
print(string)

'''
리스트

리스트란 자료들의 모음

예를 들어 학생들의 이름을 한데 묶어 처리하고 싶을때 리스트를 만들어 처리할 수 있다
name = [andy, barbie, cathie, danny, eddie]처럼 이름을 하나의 리스트에 담을 수 있다

문자열과 동일하게 요소는 0부터 시작, 마직막에서 셀때는 -1에서 시작한다

리스트에는 리스트를 넣을 수도 있는데 그것을 닺ㅇ 리스트라 한다
예를 들어 학생들의 이름을 넣고 싶은데 학급마다 다르게 저장하고 싶은 경우

name = [['andy', 'barbie'],['cathie', 'danny'], ['eddie']]
처럼 리스트 안에 리스트를 넣을 수 있다
이때 name 이라는 리스트의 0번째 요소는 ['andy', 'barbie'] 두명의 이름을 담고있는 리스트이다
그럼 andy의 이름 만을 뽑고 싶은 경우는 어떡하면 될까
name[0][0] 과 같이 불러주면 name이라는 0번재 요소의 리스트에서 0번째 요소를 불러오게 된다
'''

name = [['andy', 'barbie'],['cathie', 'danny'], ['eddie']]
print(name[0])
print(name[0][0])

'''
리스트 활용하기

리스트끼리 더하기

리스트는 문자열과 마찬가지로 서로 합칠 수 있다
예를 들어 
a=[1,2,3]
b=[4,5.6]
과 같이 두개의 리스트가 존재할때 a+b를 하면
[1,2,3,4,5,6]처럼 두 리스트를 합치게 된다

또 *를 써서 같은 리스트를 반복시키는 것도 가능하다
'''

a=[1,2,3]
b=[4,5,6]
print(a+b)
print(a*2)

#슬라이싱은 문자열과 동일
a=[1,2,3]
print(a[2])
a[2] = 4
print(a)

#1:2 인 경우 2는 포함 되지 않으므로 1번 요소만 바뀐다
#그러나 1:2 로 슬라이싱 하는것과 a[1]로 슬라이싱 하는것은 결과가 다르다
a[1:2] = ['a', 'b', 'c']
print(a)
a=[1,2,4]
a[1] = ['a', 'b', 'c']
print(a)

'''
리스트의 요소 삭제, 추가

삭제 하는 경우 : 빈 리스트를 이용하거나 del이라는 함수를 사용
추가 하는 경우 : append 라는 함수를 이용
'''

a=[1,2,3]
a[1:2] = []
print(a)
b=[1,2,3]
del b[1]
print(b)

#append는 마직 요소에 값을 삽입
#pop은 마지막 요소를 제거
c=[1,2,3]
c.append(4)
print(c)
c.pop()
print(c)

'''
튜플 

튜플은 리스트와 동일하나 안에 값을 바꿀 수 없다
'''

#이러면 에러남
a=(1,2,3)
del a[1]
