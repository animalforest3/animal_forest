#up&down 주석

#random, time, os 생성 및 기록
import random
import time
import os

# 파일 이름
filename = "myranking.txt"

# 1) 파일 없으면 생성
if not os.path.exists(filename):
    # 파일을 쓰기 모드(w) 로 새로 생성 "w"는 없으면 만들고, 있으면 내용 지움
    f = open(filename, "w", encoding="utf-8")
    #파일 사용 끝 → 반드시 닫기
    f.close()

# 2) 파일에서 랭킹 불러오기
# 파일에서 읽은 랭킹 정보를 [이름, 시도횟수, 시간] 형태로 저장할 리스트
ranking = []

#파일을 읽기 모드(r) 로 열기
f = open(filename, "r", encoding="utf-8")
#파일의 모든 줄을 리스트로 읽음
lines = f.readlines()
#파일 닫기
f.close()

#파일의 각 줄을 하나씩 처리
for line in lines:
    line = line.strip()  # 줄 끝 개행 제거
    #빈 줄이면 무시하고 다음 줄로
    if line == "":
        continue

    parts = line.split(",")   # ["3", "철수님"]
    #데이터가 3개가 아니면 (형식이 이상하면) 무시
    if len(parts) != 2:
        continue

    # "회" 글자를 제거하고 숫자만 남김
    count_str = parts[0].replace("회", "").strip()
    # 이름 문자열 저장
    name = parts[1].strip()

    # 시도 횟수가 숫자일 경우만 저장
    if count_str.isdigit():
        ranking.append([name, int(count_str)])

# 난이도 선택 함수
def select_level():
    #참일 때까지 반복
    while True:
        #오류가 날 수 있는 코드
        try:
            #사용자가 입력한 값을 level에 저장
            level = int(input(
                "난이도를 선택하세요.\n"
                "1: 쉬움(1-50)  2: 보통(1-100)  3: 어려움(1-500): "
            ))

            #1,2,3 중 하나를 선택 시 최댓값 반환
            if level == 1:
                return 50
            elif level == 2:
                return 100
            elif level == 3:
                return 500
            #1~3 숫자를 고르지 않을 경우
            else:
                print("1~3 중에서 선택해주세요.")

        #숫자가 아닌 문자를 입력할 경우
        except ValueError:
            print("숫자만 입력해주세요.")


# 게임 실행 함수
def play_game(max_num, rank):
    #정답 = 1부터 max_num까지 랜덤 숫자 생성
    answer = random.randint(1, max_num)
    #카운트는 0으로 시작
    count = 0

    #참일 때까지 반복
    while True:
        #오류가 날 수 있는 코드
        try:
            #사용자가 입력한 값을 num에 저장
            num = int(input("숫자 입력: "))
        #숫자가 아닌 문자를 입력할 경우
        except ValueError:
            print("숫자만 입력해주세요.")
            continue

        #입력할 때 하나씩 카운트
        count += 1

        #사용자가 입력한 값이 정답이면
        if num == answer:
            print(f"정답입니다! {answer} / 시도 횟수 {count}회")

            #이름 입력
            name = input("이름을 입력해주세요: ")
            #현재 시간을 초 단위로 저장 (기록용)
            now = time.time()
            #랭킹 리스트에 이름과 시도 횟수 저장
            rank.append([name, count, now])
            print("랭킹에 저장되었습니다.")

            # txt 파일에도 즉시 저장
            # 랭킹 리스트를 시도 횟수(x[1]) 기준으로 오름차순 정렬
            rank.sort(key=lambda x: x[1])
            # 파일을 쓰기 모드(w)로 열기
            # 기존 내용은 모두 지워지고 새로 작성
            f = open(filename, "w", encoding="utf-8")
            # 파일 맨 위에 제목 문구 작성
            f.write("my ranking 찾기\n")
            f.write("-----------------\n")
            # 정렬된 랭킹 리스트를 하나씩 꺼내기
            for r in rank:
                # "시도횟수 회,이름" 형식으로 파일에 저장
                f.write(f"{r[1]}회,{r[0]}\n")
            # 파일 사용이 끝났으므로 반드시 닫기
            f.close()

            #사용자가 입력한 값을 restart에 저장
            restart = input("다시 도전하시겠습니까? (Y/N): ").upper() #문자열을 전부 대문자로 변환
            return restart

        #사용자가 입력한 값이 정답보다 크면
        elif num > answer:
            print("DOWN")
        #사용자가 입력한 값이 정답보다 작으면
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
    #랭킹 정보 저장
    rank = ranking

    #참일 때까지 반복
    while True:
        #오류가 날 수 있는 코드
        try:
            #사용자가 입력한 값을 start에 저장
            start = int(input(
                "게임을 시작하시겠습니까? "
                "1) 게임 시작  2) 랭킹 보기  3) 도움말  4) 관리자 모드  5) 게임 종료: "
            ))
        #숫자가 아닌 문자를 입력할 경우
        except ValueError:
            print("숫자만 입력해주세요.")
            continue

        # 게임 시작
        #1 선택 시
        if start == 1:
            #참일 때까지 반복
            while True:
                #난이도 선택 후 최댓값 반환
                max_num = select_level()
                #5부터 1까지 1씩 감소
                for i in range(3, 0, -1):
                    time.sleep(1)
                    print(i)

                print("게임 시작")

                #게임 실행 후 다시 도전 여부 반환
                restart = play_game(max_num, rank)

                # Y가 아니면 메뉴로
                if restart != 'Y':
                    break

        # 랭킹 보기
        #2 선택 시
        elif start == 2:
            print("랭킹 TOP 5")

            #랭킹이 비어 있을 경우
            if len(rank) == 0:
                print("랭킹이 아직 없습니다.")
            else:
                #시도 횟수가 적은 순으로 정렬
                rank.sort(key=lambda x: x[1])
                #최대 5위까지 출력
                for i in range(min(5, len(rank))):
                    print(f"{i+1}위: {rank[i][0]} - {rank[i][1]}회")

        
        #3 선택 시 도움말 함수
        elif start == 3:
            show_help()

        #4 선택 시
        elif start == 4:
            print("관리자 모드")

        #5 선택 시
        elif start == 5:
            print("게임 종료")
            #종료
            break

        else:
            print("잘못 입력하셨습니다.")


# 실행
game()