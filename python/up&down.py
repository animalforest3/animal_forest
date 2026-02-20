import random as rd
import time

rank = []

#메뉴 선택
while True:
    start = int(input("게임을 시작하시겠습니까?  1) 게임 시작  2) 랭킹 보기  3) 도움말  4) 관리자 모드  5) 게임 종료:  "))
    if start == 1:
        #난이도 선택
        while True:
            print("난이도를 선택하세요.")
            level = int(input("1: 쉬움(1-50)  2: 보통(1-100)  3: 어려움(1-500):  "))
        
            if level == 1:
                max_num = 50
            elif level == 2:
             max_num = 100
            elif level == 3:
             max_num = 500
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue
            print("게임 시작")

            answer = rd.randint(1,max_num)
            count = 0

            #게임 실행
            while True:
                num = int(input('숫자 입력:  '))
                count += 1
                if num == answer:
                    print(f"정답입니다! {answer}이었고, 시도 횟수는 {count}회 입니다.")

                    name = input("이름을 입력해주세요:  ")
                    now = time.time()
                    rank.append([name, count, now])
                    print("랭킹에 저장되었습니다.")

                    restart = input('다시 도전? (Y/N):  ')
                    if restart == 'Y':
                        print("난이도 선택으로 돌아갑니다.")
                        break
                    else:
                        print("메뉴로 돌아가기")
                        break
                elif num > answer:
                    print('DOWN')
                elif num < answer:
                    print('UP')

            if restart != 'Y':
                break

    elif start == 2:
        print('랭킹 TOP 5')

        if len(rank) == 0:
            print("랭킹이 아직 없습니다.")
        else:
            rank.sort(key=lambda x: (x[1], x[2], x[0]))
            #x[1]	시도 횟수	적게 시도한 사람이 위
            #x[2]	시간	동점일 때 먼저 맞춘 사람 위
            #x[0]	이름	시도횟수 + 시간 같으면 가나다순

        for i in range(min(5, len(rank))):
            print(f"{i+1}위: {rank[i][0]} - {rank[i][1]}회")
            #rank[i] = i번째 사람 기록
            #rank[i][0] = 그 사람의 이름

        print()

    elif start == 3:
        print('도움말')

    elif start == 4:
        print('관리자 모드')

    elif start == 5:
        print('게임 종료')
        break

    else:
        print('error')


# 1. 관리자 모드 기능 1개 랭킹 초기화/1개는 임의 기능 추가
# 2. 도움말 -> 설명서
# 3. 힌트 -> 십의 자리(반환) 반복횟수 3번/5번 -> 십의자리 /기능추가