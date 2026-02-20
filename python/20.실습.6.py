#while문을 사용해서
# 1을 누르면 "게임 시작"
# 2를 누르면 "게임 종료" -> while 종료됨
# x = input("1.게임시작, 2.게임종료") #고정

while True:
    x = input("1. 게임 시작, 2. 게임 종료")
    if x == "1":
        print("게임을 시작합니다.")
    elif x == "2":
        print("게임을 종료합니다.")
        break