#자료구조 - 리스트/튜플/딕셔너리/셋
nums = [1,2,3] #리스트 : 순서가 있고, 값을 바꿀 수 있다.
num = (1,2,3) #튜플 : 순서가 있지만, 값을 바꿀 수는 없다.
person = {"name1":"김병철", "name2":"홍길동"} #딕셔너리: 이름:값(키:값)
u = {1,2,3} #셋 : 중복을 허용하지 않는 구조입니다.

#리스트
nums = [1,2,3]
print(nums[1]) #2
print(nums[2]) #3, 인덱스 번호
#값 변경
nums[2] = 25
print(nums)
nums2 = [34,23,78]
print(nums+nums2)
print(nums*3)
print(type(nums))
#구조 변경 - 리스트 반복문
for n in nums2:
    print(n*3)
for n in range(len(nums2)): #3  0 1 2 
    print(n*4)
#리스트 슬라이싱
nums = [10,20,30,40,50]
print(nums[1:4]) #range
print(nums[:4])
print(nums[2:])
print(nums[::2])
print(nums[::-1])
#[20, 30, 40]
# [10, 20, 30, 40]
# [30, 40, 50]
# [10, 30, 50]
# [50, 40, 30, 20, 10]

scores = [70, 75, 65, 43, 14] #-3 -2 -1 0 1 2 3 4
r_scores = scores[-3:]
print(r_scores) #[65, 43, 14] 최근 점수를 받겠다.
[70, 75, 65, 43, 14] #시간복잡도 공간복잡도

#리스트 메서드 - 도구, 방법
#리스트.메서드()
nums = []
# nums = 0
nums.append("이서진") #이름 추가 #순서 바꾸려면 ctrl+X, v
nums.append(12) #12 추가
nums.append([10, 20]) #1, 20 추가
print(nums)
#2차원 리스트 ['이서진', 12, [10, 20]]
print(nums[2][1]) #20 만 꺼내기 
nums.insert(0, 20) #원하는 위치에 값을 넣기
print(nums) #[20, '이서진', 12, [10, 20]]
nums.extend("이서진") #값을 연장하기 [20, '이서진', 12, [10, 20], '이', '서', '진'] 
nums.extend(["이서진"]) #[20, '이서진', 12, [10, 20], '이', '서', '진', '이서진']
print(nums)

scores = [70, 75, 65, 43, 14]
for s in scores:
    if s >= 75:
        nums.append(s)
print(nums)

#삭제
nums.remove(20) #지정 값 삭제
print(nums)
#삭제2 - pop() 인덱스로 삭제 및 변환
last = nums.pop(2) #[10, 20] 저장 후 삭제
nums.pop(3) #삭제
print(last)
print(nums)
#삭제3
del nums[0]
print(nums)
#삭제4
# nums.clear()
# print(nums)
# 리스트 길이 확인 - len
print(len(nums)) #정수 - range(len*)
#개수(탐색) - count
print(nums.count(12))
#위치 찾기(탐색) - index
print(nums.index(12))

#순서 정렬 - sort()
nums = [30, 10 ,20]
#nums.sort(reverse=True) #False 오름차순 / True 내림차순
#뒤집기 - reverse()
nums.reverse()
print(nums)

