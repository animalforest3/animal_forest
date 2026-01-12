#로또번호 추출기
# import = random
# lotto = []
# a = random.randint(1,45)
# lotto.append
#중복 없이
#멤버쉽 연산자 in / not in
# a = 40 
# b = [12,40,45]
# if a in b: #포함되어 있다면
#     print("있다!")
# else:
#     print("없다!")

# if a in b: #포함되어 있지 않다면
#     print("없다!")
#     append()
# else:
#     print("있다!")

# [1,2,3,6,5,4] 6개가 출력 되었다
#1회 2회 3회
#정렬 sort
#int
# 결과 
# 1회: 1 2 3 4 5 6
# 2회: 2 23 24 41 42 43

import random as rd
history = []

while True:
    start = int(input("추출을 시작하시겠습니까? 1) 추출 시작   2) 이력 보기   3) 종료:  "))

    if start == 1:
        lotto = rd.sample(range(1,46), 6) #sample() 함수는 중복 없이 랜덤하게 선택할 때 사용
        lotto.sort()

        print("추천 로또번호: ", end=" ")
        for num in lotto:
            print(num, end=" ")

        history.append(lotto)

    elif start == 2:
        print("추천된 이력")

        if len(history) == 0:
            print("아직 추천된 이력이 없습니다.")
        else:
            for i, nums in enumerate(history, start=1): 
                #enumerate() 함수는 리스트를 반복할 때 순서 번호도 같이 가져오게 해줌
                #for 번호, 값 in enumerate(리스트, start=번호시작):
                print(f"{i}회: ", *nums)

    elif start == 3:
        print("프로그램 종료")
        break

    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")



# import random as rd

# history = []

# while True:
#     print("\n로또 번호 추출기")
#     print("1) 추출 시작")
#     print("2) 이력 보기")
#     print("3) 종료")

#     start = int(input("선택: "))

#     if start == 1:
#         print("\n1) 자동 추첨")
#         print("2) 수동 입력")
#         mode = int(input("선택: "))

#         lotto = []

#         # 자동 추첨
#         if mode == 1:
#             lotto = rd.sample(range(1, 46), 6)

#         # 수동 입력
#         elif mode == 2:
#             cnt = int(input("몇 개를 직접 입력하시겠습니까? (1~5개): "))

#             for i in range(cnt):
#                 num = int(input(f"{i+1}번째 숫자 입력 (1~45): "))

#                 if num < 1 or num > 45 or num in lotto:
#                     print("잘못된 입력입니다.")
#                     break

#                 lotto.append(num)

#             # 부족한 개수 자동 채우기
#             need = 6 - len(lotto)

#             auto_nums = rd.sample(
#                 [n for n in range(1, 46) if n not in lotto],
#                 need
#             )

#             lotto.extend(auto_nums)

#         else:
#             print("잘못된 선택")
#             continue

#         lotto.sort()

#         print("\n추천 로또번호:", *lotto)
#         history.append(lotto)

#     elif start == 2:
#         print("\n추천된 이력")
#         if len(history) == 0:
#             print("이력이 없습니다.")
#         else:
#             for i, nums in enumerate(history, start=1):
#                 print(f"{i}회:", *nums)

#     elif start == 3:
#         print("프로그램 종료")
#         break

#     else:
#         print("잘못된 입력입니다.")