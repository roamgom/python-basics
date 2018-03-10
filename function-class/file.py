# 파일 생성
# 상대 주소
f = open("file.txt", 'w')
f.close()

# 절대 주소
f = open("C:/some_dir/file.txt", 'w')
f.close()

# 파일 적기
f = open("file.txt", 'w')
for i in range(1, 11):
    data = "{} Line".format(i)
    data = "%d Line" % i
    f.write(data)
f.close()

# 파일 한줄 읽기
f = open("file.txt", 'r')
line = f.readline()
print(line)
f.close()

# 파일 모든 줄 읽기
f = open("file.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 모든 줄 읽기
f = open("file.txt", 'r')
data = f.read()
print(data)
f.close()

# 모든 줄 읽기
f = open("file.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)

# 특정 줄만 읽기
for line in lines[2:5]:
    print(line)
f.close()

# 내용 추가
f = open("file.txt", 'a')
for i in range(10):
    data = "%d Line" % i
    f.write(data)
f.close()

# with 문
with open("file.txt", 'w') as f:
    f.write("Hello, Python")

# sys 모듈로 입력 인수 (선택사항)
# sys_01.py
import sys

args = sys.argv[1:]
for i in args:
    print(i)

# python3 sys_01.py aaa bbb ccc

# 예제
# sys_02.py
import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
# python3 sys_02.py hello python
# HELLO PYTHON