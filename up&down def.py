#up&down 문자열+예외처리
import random as rd
import time
import os

filename = "myranking.txt"

# 1) 파일 없으면 생성
if not os.path.exists(filename):
    f = open(filename, "w", encoding="utf-8")
    f.close()

# 2) 파일에서 랭킹 불러오기
ranking = []

f = open(filename, "r", encoding="utf-8")
lines = f.readlines()
f.close()

for line in lines:
    line = line.strip()  # 줄 끝 개행 제거
    if line == "":
        continue

    parts = line.split(",")   # ["3", "철수"]
    if len(parts) != 2:
        continue

    count_str = parts[0].replace("회", "").strip()
    name = parts[1].strip()

    # 시도 횟수가 숫자일 경우만 저장
    if count_str.isdigit():
        ranking.append([name, int(count_str)])

# 난이도 선택 함수
def select_level():
    while True:
        try: #오류가 날 수 있는 코드
            level = int(input(
                "난이도를 선택하세요.\n"
                "1: 쉬움(1-50)  2: 보통(1-100)  3: 어려움(1-500): "
            ))

            if level == 1:
                return 50
            elif level == 2:
                return 100
            elif level == 3:
                return 500
            else: #1~3 숫자를 고르지 않을 경우
                print("1~3 중에서 선택해주세요.")

        except ValueError: #숫자가 아닌 문자를 입력할 경우
            print("숫자만 입력해주세요.")


# 게임 실행 함수
def play_game(max_num, rank):
    answer = rd.randint(1, max_num)
    count = 0

    while True:
        try: #오류가 날 수 있는 코드
            num = int(input("숫자 입력: "))
        except ValueError: #숫자가 아닌 문자를 입력할 경우
            print("숫자만 입력해주세요.")
            continue

        count += 1

        if num == answer:
            print(f"정답입니다! {answer} / 시도 횟수 {count}회")

            name = input("이름을 입력해주세요: ")
            now = time.time()
            rank.append([name, count])
            print("랭킹에 저장되었습니다.")

            # txt 파일에도 즉시 저장
            rank.sort(key=lambda x: x[1])
            f = open(filename, "w", encoding="utf-8")
            f.write("my ranking 찾기\n")
            f.write("-----------------\n")
            for r in rank:
                f.write(f"{r[1]}회,{r[0]}\n")
            f.close()

            restart = input("다시 도전하시겠습니까? (Y/N): ").upper() #문자열을 전부 대문자로 변환
            return restart

        elif num > answer:
            print("DOWN")
        else:
            print("UP")

# 도움말 함수
def show_help():
    print("""
도움말 - 게임 방법

1. 난이도를 선택하면 숫자의 범위가 정해집니다.
   - 쉬움  : 1 ~ 50
   - 보통  : 1 ~ 100
   - 어려움: 1 ~ 500

2. 숫자를 입력하고 정답을 맞히면 랭킹이 저장됩니다.
""")


# 메인 게임 함수
def game():
    rank = ranking

    while True:
        try:
            start = int(input(
                "게임을 시작하시겠습니까? "
                "1) 게임 시작  2) 랭킹 보기  3) 도움말  4) 관리자 모드  5) 게임 종료: "
            ))
        except ValueError:
            print("숫자만 입력해주세요.")
            continue

        # 게임 시작
        if start == 1:
            while True:
                max_num = select_level()
                for i in range(3, 0, -1):
                    time.sleep(1)
                    print(i)

                print("게임 시작")

                restart = play_game(max_num, rank)

                if restart != 'Y':
                    break

        # 랭킹 보기
        elif start == 2:
            print("랭킹 TOP 5")

            if len(rank) == 0:
                print("랭킹이 아직 없습니다.")
            else:
                rank.sort(key=lambda x: x[1])
                for i in range(min(5, len(rank))):
                    print(f"{i+1}위: {rank[i][0]} - {rank[i][1]}회")

        elif start == 3:
            show_help()

        elif start == 4:
            print("관리자 모드")

        elif start == 5:
            print("게임 종료")
            break

        else:
            print("잘못 입력하셨습니다.")


# 실행
game()