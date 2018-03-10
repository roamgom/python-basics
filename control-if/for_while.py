'''
반복문은 같은 동작을 여러번 하고싶을때 사용합니다
반복문은 주로 for while 두가지의 함수를 사용하는데
while문 같은 경우 무한루프를 돌릴때 자주 사용합니다

그럼 이제 각 함수별 사용 방법을 알아 봅시다

for 반복할 변수이름 in 반복할 내용에 관한 문장:
  |
  |반복할 문장

그냥 봐서는 감이 잘 안잡히시죠
그래서 반복문에 자주 쓰이는 함수를 몇개 준비해 봤습니다
바로 len 과 range 라는 친구들 입니다

len(변수) : 변수의 길이를 나타냅니다
	ex) a=[1,2,3,4], b=['a','b','c'], c=4, d=[1,2,[1,2]]
	    len(a)=4     len(b)=3         정수는 길이가 없다 len(d[2]=2)
range(시작점. 끝점) : 시작점(정수) <= x < 끝점(정수)
			위와 같은 범위에 있을 수 있는 x의 값을 갖고있는 자료형
'''

#ex) 0부터 9까지의 정수를 리스트에 저장하고
#   리스트의 각 요소들을 두배로 만드는 프로그램

a=[]
for i in range(10):
  a.append(i)
for i in range(len(a)):
  a[i] = a[i]*2
print(a)

'''
그럼 이제 while문에 대해 알아 봅시다

while 조건 :
  |
  |반복할 내용

while문은 특별한것 없이 조건이 참일 경우 계속 반복 합니다
그러므로 일정 횟수만큼 반복하고 싶다면 증감식을 안에 넣어야 되죠

while i<=10:
  print("hi")
  i+=1

위와 같이 말이죠
위의 반복을 for 문으로 한다면

for i in range(10):
  print("hi")

이렇게 됩니다
for가 훨씬 간단하죠?

그럼 while은 언제 사용 하느냐
앞서 설명드렸다 시피 무한루프를 돌릴때 사용합니다
예제를 통해 알아보겠습니다
'''

#ex) id 와 비밀번호를 입력받아 로그인 시키는 프로그램
Id = 'eddie' # 우리의 아이디
password = 'jongmin' # 우리의 비밀번호

while True:
    new_id = input() # 입력받을 아이디
    new_pass = input() # 입력받을 비밀번호
    id_ok = False # 아이디가 일치하는가?
    pass_ok = False # 비밀번호가 일치하는가?

    for i in range(len(new_id)):    #입력받은 아이디만큼 반복
        if new_id[i] is Id[i]:    #입력받은 아이디의 i번째 문자가 우리의 id의 i 번째 문자와 같은가?
            id_ok = True # 맞으면 참
        else: #아니면 거짓
            id_ok = False
            break # 이미 거짓임을 알았기 때문에 더이상 수행할 필요가 없음

    for i in range(len(new_pass)): # 비밀번호로 반복
        if new_pass[i] is password[i]:
            pass_ok = True
        else:
            pass_ok = False
            break

    if pass_ok and id_ok: #아이디 비번 둘다 맞으면 루프를 탈출
        break
    else:
        pass

#과제
#피보나치