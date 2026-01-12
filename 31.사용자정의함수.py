#사용자 정의 함수 def
def show_student():
    print("학생 목록 출력")
    print("kim - 90점")
    print("lee - 80점")

show_student()
show_student()
#조건
#1. 2번 이상 반복이 된다.
#2. while / if 구조 자체가 반복이 된다.
#3. 한 함수가 입력/처리/출력 -> 나누기
#4. 한 번 고치면 여러 곳을 고쳐야 한다.

# def 함수이름(매개변수):
#     실행할 코드

def add(a,b):   #a b는 매개변수
    return a + b    #연산을 하고, 가지고 있는다. -> 반환(돌려준다)
print(add(3,4)) #인자
print(add(35,48))

def s(a, b="안녕하세요"): #a b는 매개변수
    print(b, a)

#가변인자
def total(*args): #a b는 매개변수
    print(args)
total(1,2,3,4)  #튜플 - 변하지 않는


def sum_all(*nums): #a b는 매개변수
    total = 0
    for n in nums:
        total += n #total = total + n
    return total
print(sum_all(1,2,3,4,5))

#가변 딕셔너리
def show_info(**kwargs):
    print(kwargs)

def show_info(**info):
    for k, v in info.items():
        print(k, ":", v)
show_info(name="kim", score=80, grade="c")

def example(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs) #key=value 형태의 인자들
example(1,2,3,4,name="이서진")

#업앤다운 -> 로또번호 -> 가위바위보
#업앤다운 - 게임만 def game()
# game()
# if a ="1"
# 게임 -> game()

#전역변수 / 지역변수

#Error
# x = 10 #전역변수
# def func():
#     y = 5 #지역변수
#     print(x)
#     print(y)
#     return y
# def func1():
#     x = x + 1
#     return x
# func1()
# x = 10
# def func1():
#     return x + 1
# func1()
#실행 가능
#immutable(변경할 수 없는) vs mutable(변경할 수 있는)
#immutable
#숫자, 문자, 튜플
#mutable
#리스트, 딕셔너리, 셋
#원본 유지 x
data1 = {"x":10}
def func3(s):
    s["x"] += 1
func3(data1)
print(data1) #원본 수정 출력

#원본 유지 o
data2 = {"x":10}
def func4(s):
    data3 = s.copy() #얕은 복사
    data3["x"] += 1
    return data3
new_data = func4(data2)
print(data2) #원본
print(new_data) #수정본

# 1. 업앤다운 게임 def 묶어서 전체 코드 업로드(선행)
# 2. 업앤다운 게임 def main(), ask(), input() 입력/출력/게임
# 로또번호 메뉴 / 로또번호 실행 / 로또번호 출력, 입력