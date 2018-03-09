'''
딕셔너리

딕셔너리란 이름 그대로 사전과 같이 동작한다
사전에서 단어가 있고 그에 대응하는 뜻이 존재하듯이
딕셔너리 자료형은 key와 그에 대응하는 값인 value가 존재한다

예를 들어 학생의 이름을 넣으면 그 학생의 학년이 나오게 하고싶은 경우
딕셔너리를 쓰면 편리하다

딕셔너리를 만들 때에는 key값이 중복되어서는 안된다.
'''

dic = {
    'andy' : '1',
    'barbie' : '2',
    'cathie' : '3',
    'danny' : '4'
}

print(dic['andy'])

#딕셔너리에 값을 넣거나 빼고 싶은 경우
a={1:'a'}
a[2] = 'b'
print(a)
a['c'] = 3
print(a)

#제거하고 싶은 경우
del a['c']
print(a)

#keys 와 values
#딕셔너리 내의 key값을 반환
print(a.keys())
#딕셔너리 내의 value값 들을 반환
print(a.values())
#items
#딕셔너리 내의 key,value 쌍을 반환
print(a.items())

#딕셔너리 key값에 따른 value값을 반환
print(a.get(1))
#만약 딕셔너리 안에 key가 없을경우 반환값을 설정해 줄 수 있다
print(a.get(3,'none'))
#딕셔너리 안에 해당 키가 있는지 조사
print(1 in a)
print(3 in a)

'''
집합 자료형

집합 자료형은 집합에 관한것을 편하게 처리하기 위해 사용
집합 자료형은 딕셔너리와 마찬가지로 순서가 없고, 중복을 허용하지 않는다
'''

a = set('hello')
print(a)

#인덱싱을 위해 집합 자료형을 변환
l1 = list(a)
print(l1)
t1 = tuple(a)
print(t1)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

#교집합
print(s1 & s2)
#합집합
print(s1 | s2)
#차집합
print(s1 - s2)

#요소 추가하기
#요소 한개
s1 = set([1,2,3])
s1.add(4)
print(s1)
#요소 여러개 추가하기
s1.update([5,6,7])
print(s1)
#요소 제거하기
s1.remove(2)
print(s1)

'''
부울 자료형

부울 자료형은 참, 거짓 두가지 값 만을 갖는다
조건의 참, 거짓을 판별할때 쓰인다
'''

print(1>2)
print(1<2)

'''
논리 연산

a>b : a가 b보다 크다
a>=b : a가 b보다 크거나 같다
a<b : a가 b보다 작다
a<=b : a가 b보다 작거나 같다
a and b : a 그리고 b
a or b : a 아니면 b
a==b : a와 b가 같다
a is b : a와 b가 같다(None, True, False에서 사용)
not a : a 의 논리 반전
a is not b : a와 b가 같지 않다(None, True, False에서 사용)
a != b : a와 b가 같지 않다
a in b : a가 b의 요소다
'''

'''
과제 
집합 자료형의 요소를 여러개 제거하고 싶은 경우 어떡해야 할까

1,2,3,4,5,6 에서 3,4,5 제거하기
'''

s = set([1,2,3,4,5,6])
l1 = list(s)
l1[2:5] = []
s = set(l1)
print(s)