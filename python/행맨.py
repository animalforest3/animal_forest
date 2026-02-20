import random

# 단어 목록
fruit = ["apple", "banana", "orange", "grape", "strawberry", "peach", "cherry", "melon", "lemon", 
         "mango","kiwi","avocado","papaya","pear","fig","plum","lime","tangerine"]

# 랭킹 저장용 리스트
ranking = []

# 프로그램 시작
while True:
    print("""
===== 행맨 게임 =====
1) 게임 시작
2) 랭킹 보기
3) 규칙 보기(Help)
4) 관리자 모드
5) 종료
""")

    # 메뉴 선택
    try:
        menu = int(input("메뉴를 선택해주세요: "))
    except ValueError:
        print("숫자만 입력하세요.")
        continue

    # 1) 게임 시작
    if menu == 1:
        print("\n난이도를 선택하세요")

        try:
            level = int(input("1) 쉬움  2) 보통  3) 어려움: "))
        except ValueError:
            print("숫자만 입력하세요.")
            continue

        # 난이도 설정
        if level == 1:
            lives = 7
            level_name = "쉬움"
        elif level == 2:
            lives = 5
            level_name = "보통"
        elif level == 3:
            lives = 3
            level_name = "어려움"
        else:
            print("1~3 중에서 선택하세요.")
            continue

        answer = random.choice(fruit)   # 정답 단어
        guessed = []                    # 맞힌 알파벳
        tries = 0                       # 총 시도 횟수

        print("\n행맨 게임 시작!")

        while True:
            # 1. 매 턴 시작 시 이전 내용과 분리하기 위해 공백 출력
            print("\n" + "-"*30)
            
            # 현재 단어 상태 출력
            display = ""
            for ch in answer:
                if ch in guessed:
                    display += ch + " "
                else:
                    display += "_ "

            # 화면 출력
            print(f"[단어] {display.strip()}")
            print(f"[남은 목숨] {lives}")

            if len(guessed) == 0:
                print("[시도한 글자] 없음")
            else:
                print("[시도한 글자] " + ", ".join(guessed))

            # 승리 조건
            if "_" not in display:
                print("정답입니다!")
                name = input("이름을 입력하세요: ")
                ranking.append([name, level_name, tries])
                print("랭킹에 저장되었습니다.")
                break

            # 입력 (공백 제거 포함)
            guess = input("글자 입력(1개) : ").lower().strip()

            # [검증 1] 빈 입력 / 공백 입력
            if not guess:
                print("\n>> 아무것도 입력하지 않았습니다. 다시 입력하세요.")
                continue

            # [검증 2] 2글자 이상 입력 (요구사항 반영)
            if len(guess) > 1:
                print("\n>> 한 글자만 입력하세요.")
                continue

            # [검증 3] 숫자나 특수문자 입력 (요구사항 반영)
            if not guess.isalpha():
                print("\n>> 영문 1글자만 입력하세요.")
                continue

            # [검증 4] 이미 시도한 글자
            if guess in guessed:
                print(f"\n>> 이미 입력한 글자 : {guess}")
                print(">> 이미 시도한 글자입니다.")
                continue

            # 모든 검증을 통과한 경우에만 시도 횟수 증가 및 기록
            tries += 1
            guessed.append(guess)

            # 정답 확인 로직
            if guess not in answer:
                lives -= 1
                print(f">> 결과: 틀렸습니다! (목숨 -1)")
            else:
                print(f">> 결과: 맞았습니다! '{guess}'가 있습니다.")

            # 5. 패배 조건 (목숨 0일 때 루프 탈출)
            if lives <= 0:
                print(f"\n패배하셨습니다. 정답은 [{answer}]였습니다.")
                break

            

    # 랭킹 보기
    # 2) 랭킹 보기
    elif menu == 2:
        print("\n")
        print("실시간 랭킹 Top 5")
        print("="*40)
        
        if len(ranking) == 0:
            print("아직 등록된 랭킹이 없습니다.")
        else:
            sorted_ranking = sorted(ranking, key=lambda x: x[2])

            top_5 = sorted_ranking[:5]
            
            for i in range(len(top_5)):
                name, level, tries = top_5[i]
                print(f"{i+1}위 | 이름: {name:8s} | 난이도: {level} | 시도횟수: {tries}회")
        
    # 규칙 보기
    elif menu == 3:
        print("""
게임 규칙(Help)

1. 단어는 _ 로 가려집니다.
2. 알파벳 한 글자씩 입력합니다.
3. 틀릴 때마다 기회가 줄어듭니다.
4. 모든 글자를 맞히면 승리합니다.
5. 기회를 모두 쓰면 패배합니다.
""")

    # 관리자 모드
    elif menu == 4:
        print("\n관리자 모드")

    # 종료
    elif menu == 5:
        print("게임을 종료합니다.")
        break

    else:
        print("1~5 중에서 선택하세요.")