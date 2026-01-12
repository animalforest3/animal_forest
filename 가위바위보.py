import random as rd
c = ["가위", "바위", "보"]
# 사용자가 입력을 하면 입력한 값과 랜덤으로 나온 값과 비교해서
# 승/패를 만듭니다.
# 1. 게임 시작
#   1. 3판 2선승제
#   2. 단일 게임
while True:
    start = int(input("게임을 시작하시겠습니까? 1) 게임 시작 2)게임 종료:   "))     # 사용자의 선택을 받아온다.

    # 게임 종료
    if start == 2:
        print("게임 종료")
        break

    # 게임 시작
    if start == 1:
        while True:
        # 점수를 먼저 0으로 세팅해놓는다.
            user_win = 0
            computer_win = 0
        
            while user_win < 2 and computer_win < 2:        # 점수가 2번 미만일때 계속한다.
                computer = rd.choice(c)
                user = int(input("1:가위   2:바위   3:보      :"))

                user_choice = c[user -1]    # c = ["가위", "바위", "보"]에서 -1하면 이길 수 있다.

                print("computer: ",computer)
                print("user: ", user)

                if user_choice == computer:
                    print("비겼습니다.")

                elif(
                    (user_choice == "가위" and computer == "보") or
                    (user_choice == "바위" and computer == "가위") or
                    (user_choice == "보" and computer == "바위")
                ):
                    user_win += 1   
                    print("이겼습니다.")    # 이겼다면 점수가 올라간다.

                else:
                    computer_win += 1
                    print("졌습니다.")      # 이겼다면 점수가 올라간다.

                print(f"현재    ->  사용자{user_win} : 컴퓨터{computer_win}")       # 사용자와 컴퓨터의 현재 점수

            if user_win == 2:    # 2선승
                print("사용자가 최종 승리하였습니다. 축하합니다.")
            else:
                print("컴퓨터가 최종 승리하였습니다.")

                restart = input('다시 도전하시겠습니까? (Y/N):  ')
                if restart != 'Y':      # Y가 아니라면 게임 종료, Y면 게임 시작 while로 돌아간다.
                    print("게임 종료")
                    exit()      # 게임 종료
