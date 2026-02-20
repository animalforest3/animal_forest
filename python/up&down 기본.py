import random as rd

gold = rd.randint(1,100)
count = 0
while True:
    print("1. 게임 시작")
    print("2. 종료")
    try:
        menu = int(input("메뉴를 선택하세요: "))
        if menu == 1:
            while True:
                try:
                    ans = int(input("숫자를 입력하세요: "))
                    count += 1
                    if ans > gold:
                        print("다운")
                    elif ans < gold:
                        print("업")
                    else:
                        print(f"정답입니다! {gold}이였고, 시도횟수는 {count}번이였습니다.")
                        break
                except ValueError:
                    print("숫자를 입력해주세요.")
            break
        elif menu == 2:
            print("게임을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")
    except ValueError:
        print("숫자를 입력해주세요.")