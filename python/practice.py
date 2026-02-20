#practice

# nums = [70, 75, 65, 43, 14]
# nums2 = [1, 2, 3, 4, 5]

# print(nums[1]) #2번째 숫자

# nums[1] = 25 #2번째 숫자 바꾸기
# print(nums)

# print(nums+nums2) #[70, 25, 65, 43, 14, 1, 2, 3, 4, 5]
# print(nums*3) #[70, 25, 65, 43, 14, 70, 25, 65, 43, 14, 70, 25, 65, 43, 14]

# for n in nums2:
#     print(n*3) #3 6 9 12 15

# for n in range(len(nums2)): #range(5) = 0~4
#     print(n*4) # = n(0~4) * 4

# nums3 = [10,20,30,40,50]
# print(nums3[1:4]) #20,30,40 1부터 3까지
# print(nums3[:4]) #10,20,30,40 0부터 3까지
# print(nums3[2:]) #30,40,50 2부터 끝까지
# print(nums3[::2]) #2칸씩 이동
# print(nums3[::-1]) #거꾸로

# nums = [10,20,30]
# print(nums)

# print(nums[0])
# print(nums[1])

# scores = [80,90,75,88,92]
# print("학생 점수:", scores)
# print("첫 번째 학생 점수:", scores[0])
# scores[2] = 85
# print("재채점 후:", scores)

# nums[1] = 25
# print(nums)

# a = [1,2]
# b = [3,4]
# print(a+b)
# print(a*3)

# for n in nums:
#     print(n)

# scores = [70,75,80,85,90,95]
# recent_scores = scores[-3:]
# print("최근 3명 점수:", recent_scores)

# scores = [80,90,85,75]
# avg = sum(scores)/len(scores)
# print("평균 점수:", avg)

# nums=[]
# nums.append(10)
# nums.append(20)
# nums.append([10,20])
# print(nums)

# nums=[10,30,40]
# nums.insert(1,20)
# nums.insert(4, 50)
# print(nums)

# nums=[10,20]
# nums.extend([30,40])
# print(nums)

# scores=[60,70,80,90]
# passed=[]
# for s in scores:
#     if s >= 75:
#         passed.append(s)
# print("합격 점수:",passed)

# for s in scores:
#     if s > 60:
#         passed.append(s)
# print("점수:",passed)

# nums = [10,20,30]
# nums.remove(20)
# last = nums.pop(2) # nums.pop(2)=30 반환함과 동시에 삭제, 이 값을 last에 저장한다.
# print(last) # = 30
# print(nums) #30은 삭제했기에 10,20만 출력

# del nums[1] # 다른 변수에 저장하지 않고 인덱스1에 해당하는 수를 삭제
# print(nums) #10,30

# nums.clear() # 리스트 안의 수 모두 삭제
# print(nums) # [] 빈 리스트 출력
# print(len(nums)) # 빈 리스트의 요소 개수 출력 = 0
# print(len(nums)) # 리스트의 요소 개수 출력 = 3

# nums = [10,20,20,30]
# print(nums.count(20)) # 리스트 안의 20의 개수
# print(nums.index(30)) # 리스트의 인덱스 번호

# nums = [30,10,20]
# nums.sort(reverse=False) #False오름차순 / True내림차순
# print(nums) #10,20,30 / 30,20,10

# nums.reverse()
# print(nums) #30,20,10 / 10,20,30 이전에 코드에 영향을 받음

# nums = [10,20,30] 
# print(20 in nums) #True 포함 여부
# print(40 in nums) #False 포함여부

# scores=[60,70,80,90]
# passed=[]
# for s in scores:
#     if s >= 75:
#         passed.append(s)
# print("합격점수:",passed)
# print("최고 점수:",max(scores))
# print("최저 점수:",min(scores))

# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# num = 1
# while True:
#     if num == 5:
#         break
#     print(num)
#     num += 1

# num = 0
# while num < 10:
#     num += 1
#     if num % 2 == 0: #홀수값만 나옴 num:짝수
#         continue
#     print(num) 

# num = 0
# while num < 10:
#     num += 1
#     if num % 2 == 1: #짝수값만 나옴 num:홀수
#         continue
#     print(num)

# i = 1
# while i <= 3:
#     j=1
#     while j <= 3: 
#         print(i,j)
#         j += 1
#     i += 1
# i가 한번 돌 동안 j가 3번 돌음
# while j에서 j=3이 끝나고 j=+1로 인해 j=4가 되면 while j <= 3에서 False가 나오기 때문에 더이상 반복하지 않고 빠져나온다
# i =+ 1 진행해서 i=2가 되고, 다시 j 반복문 진행

# total = 0
# for i in range(1,11):
#     if i % 2 == 0: # i:짝수
#         total += i # i가 짝수일때만 tatal의 값이 쌓임
# print(total) # 30

# num = 1
# while num <= 10:
#     if num % 2 == 0: # num:짝수
#         print(num)
#     num += 1 #while문 반복문

# score = 50
# while score <= 80:
#     if score >= 60:
#         print(score,"합격")
#     else:
#         print(score,"불합격")
#     score += 10

# score = 95
# while score >= 50:
#     if score >= 90:
#         grade = "A"
#     elif score >= 70:
#         grade = "B"
#     else:
#         grade = "C"

#     print(score,grade)
#     score -= 15
#     # score=95부터 시작해서 print까지 간 후에 -15씩 진행, score가 5보다 크거나 같을때 까지

# name = "이서진"
# age = "24"
# x = "제 이름은 "+name+"이고, 나이는 "+age+"살 입니다."
# print(x)

# for dan in range(1,5):
#     print(dan, "단")
#     for num in range(1,10):
#         print(dan * num)

# person = {"name": "kim", "age": 30}
# print(person["name"])
# print(person["age"])

# person["age"] = 31  #수정
# person["city"] = "seoul"    #추가
# print(person)

# #학생 정보 저장하기
# student = {"name":"민수","age":20}
# student["age"] = 21
# student["major"] = "컴퓨터 공학"
# print(student)

# person = {"name": "kim", "age": 30}
# for k in person:
#     print(k)    #key name,age
#     print(person[k])    #value  person[k] = 그 key에 해당하는 value

# def game():
#     print("게임 시작")

# print("프로그램 시작")
# game()

# def show_students():
#     print("학생 목록 출력")
#     print("모르겠어요")
# show_students()

# def add(a,b):
#     return a + b
# print(add(3,4))
# print(add(183,385))

# def greet(name="이서진",msg="안녕하세요"):
#     print(msg,name+"입니다")
# greet()

# def total(*args): 
#     print(args)
# total()

# def sum_all(*nums):
#     total = 0
#     for n in nums:
#         total += n
#     return total
# print(sum_all(1,2))
# print(sum_all(1,2,3,4))
# #영향을 미침(sum_all)
# def avg_all(*scores):
#     return sum_all(*scores) / len(scores)
# print(avg_all(80,90,100))

# def show_info(**kwargs):
#     print(kwargs)

# def print_student(**info): #info:딕셔너리 형태
#     for k, v in info.items(): #k=키 v=값
#         print(k, ":", v) #이 형태대로 출력해달라
# print_student(name="lee", score=90, grade="A") #입력 값

# # *args - 인자의 개수가 정해지지 않음
# # **kwargs - 여러개의 키워드 인자

# # return이 있음
# def build_student(**info): #info:딕셔너리 형태
#     return info 
# student = build_student(name="Lee", scores=[80, 85, 90]) #info에 저장 후 student에 저장
# print(student)

#간단하게 게임 만들기
import random
def small_game():
    y = int(input("시작? 1 or 2:    "))
    z = random.randint(1, 100)
    if y == 1:
        print("1~100")
        while True:
            x = int(input("x:   "))
            if x > z:
                print("too big")
            elif x < z:
                print("too small")
            else:
                print("correct")
                print("game over")
                exit()
    else:
        print("종료")

small_game()
#함수, while, if문 정리 완료