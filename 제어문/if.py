'''
조건문

우선 프로그래밍을 하는데 있어 조건문과 반복문은 빠질 수 없는
필수 요소라 해도 과언이 아닐 정도로 많이 사용됩니다
따라서 여러분은 조건문과 반복문을 숙달하여 자신의
팔다리 처럼 사용할 수 있어야 합니다

그럼 파이썬 에서의 조건문과 반복문을 알아보도록 합시다

우선 조건문은 총 세가지 함수
if
elif
else
가 존재합니다

if 조건 :
  |(|줄친 부분은 항상 동일하게 빈칸이 들어가야 됩니다)
  |
  |조건이 참일 경우
  |수행할 문장들

위와 같은 형태로 사용합니다(':'을 꼭 넣어주세요)
그러나 if는 한번에 여러가지 조건들을 넣기
어렵기 때문에 elif 라는 함수역시 존재합니다
elif 는

if 조건 :
  |
  |
  |조건이 참일 경우
  |수행할 문장들
elif 조건 :
  |
  |
  |조건이 참일 경우
  |수행할 문장들

위와 같은 형태로 사용하지요

또, 여러분이 상정한 조건들을 전부 만족시키지 못한 경우를
위해 else라는 함수도 존재합니다
else는 위의 조건을 전부 만족시키지 않은 경우에만
기능을 수행하므로 따로 조건을 달지 않습니다

if 조건 :
  |
  |
  |조건이 참일 경우
  |수행할 문장들
elif 조건 :
  |
  |
  |조건이 참일 경우
  |수행할 문장들
else:
  |
  |수행할 문장

위와 같은 형태가 조건문의 완성형입니다

또 조건문을 사용할 경우 논리연산은 필수로 사용되기 때문에 정리해
놓겠습니다

input() 함수

input("질문 내용") 으로 프롬프트에서 사용자로부터 입력을 받을 수 있다
input()은 항상 문자열로 저장하기 때문에 다른 자료형으로 바꾸고 싶을 때는
자료형(input())으로 자료형을 바꿔줘야 된다

자료형별 이름
정수형 : int
실수형 : float
문자열 : str
리스트 : list
튜플 : tuple
'''

#예제 코드
math = int(input())
english = int(input())
science = int(input())
society = int(input())

avg = (math+english+science+society)/4

if avg <= 90 and avg > 80:
    print("A")
elif avg <= 80 and avg >70:
    print("B")
elif avg <=70 and avg > 60:
    print("C")
else:
    print("D")

#