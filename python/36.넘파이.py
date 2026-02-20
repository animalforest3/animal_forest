# #넘파이 Numpy
# import numpy as np #seed 값을 고정하는 함수 - 키

# np.random.seed(42)

# a = np.array([10, 20, 30])
# print("a:", a) #행과 열
# print("a.shape:", a.shape) 

# # arange / reshape
# b = np.arange(1, 13).reshape(3, 4) #arrange 값을 추출 -> 3행과 4열
# print("b:\n", b)

# # 기본 통계
# print("b.sum():", b.sum())
# print("b.mean():", b.mean())
# print("b.max():", b.max())
# print("b.min():", b.min())

# # 난수
# r1 = np.random.rand(3)          # 0~1
# r2 = np.random.randint(1, 11, size=5)  # 1~10
# print("rand(3):", r1)
# print("randint(1~10, 5개):", r2)



# import numpy as np
# a = np.array([10, 20, 30])
# print(a.shape)   # (3,)

# a = np.array([10, 20, 30])

# a_1x3 = a.reshape(1, 3)
# a_3x1 = a.reshape(3, 1)

# print(a_1x3)
# print(a_1x3.shape)

# print(a_3x1)
# print(a_3x1.shape)



# import random
# import os

# filename = "ranking.txt"

# # 1) 파일 없으면 생성
# if not os.path.exists(filename):
#     f = open(filename, "w", encoding="utf-8")
#     f.close()

# # 2) 파일에서 랭킹 불러오기 -> [[tries, name], [tries, name], ...]
# ranking = []

# f = open(filename, "r", encoding="utf-8")
# lines = f.readlines() # 한 줄 씩
# f.close()

# for line in lines: # 시도횟수, 이름\n
#     line = line.strip()  # 줄 끝 개행 제거 시도횟수, 이름 """
#     if line == "":
#         continue

#     parts = line.split(",")   # ["3", "철수"]
#     if len(parts) != 2:
#         continue

#     tries_str = parts[0].strip()
#     name = parts[1].strip()

#     # tries가 숫자인지 간단히 확인
#     if tries_str.isdigit():
#         tries = int(tries_str)
#         ranking.append([tries, name])

# # 3) 기존 TOP5 출력
# ranking.sort()  # tries(시도횟수) 기준 오름차순 정렬 (리스트 첫 값 기준)
# print("\n===== 기존 랭킹 TOP 5 =====")
# if len(ranking) == 0:
#     print("아직 랭킹 기록이 없습니다.")
# else:
#     top = ranking[:5]
#     for i in range(len(top)): # 0 1 2 3 4
#         print(f"{i+1}위) {top[i][1]} - {top[i][0]}회")
# print("==========================\n")


# # -------------------
# # 4) 업앤다운 게임 시작
# # -------------------
# answer = random.randint(1, 2)
# tries = 0

# print("업앤다운 게임 시작! (1~100)")
# while True:
#     guess = input("숫자 입력: ")

#     if guess.isdigit() == False:
#         print("숫자만 입력해 주세요.")
#         continue

#     guess = int(guess)
#     tries += 1

#     if guess < answer:
#         print("UP")
#     elif guess > answer:
#         print("DOWN")
#     else:
#         print(f"정답! {tries}번 만에 맞췄습니다.")
#         break

# # 5) 닉네임 입력 받고 랭킹에 추가
# name = input("닉네임을 입력하세요: ").strip()
# if name == "":
#     name = "익명"

# ranking.append([tries, name])

# # 6) txt 파일에도 즉시 저장(한 줄 추가)
# f = open(filename, "a", encoding="utf-8")
# f.write(f"{tries},{name}\n") # 이스케이프 문자/함수 \n
# f.close()

# # 7) 정렬 후 TOP5 출력
# ranking.sort()

# print("\n===== 최신 랭킹 TOP 5 =====")
# top = ranking[:5]
# for i in range(len(top)):
#     print(f"{i+1}위) {top[i][1]} - {top[i][0]}회")
# print("==========================")



import random 
import time
answer = random.randint(1,2)
while True:
    print("메뉴를 입력하세요")
    print("게임을 시작합니다.")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    s = input("숫자 입력(종료 q): ")
    if s == "q":
        break                 # 게임 종료
    try:
        guess = int(s)
    except:
        print("숫자만 입력!")
        continue              # 잘못 입력 → 다시 입력
    # 여기부터는 정상 숫자만 들어온 상태
    if guess < answer:
        print("UP")
    elif guess > answer:
        print("DOWN")
    else:
        print("정답!")
        break                 # 정답이면 반복 끝(게임 끝)