# save = []
# def lott():
#     global save
#     save.append([1,2,3,4,5,6])

# save = []
# def lott():
#     save.append([1,2,3,4,5,6])
# save = ([1,2,3,4,5,6])

# def reset_wrong():
#     save = []

# reset_wrong()
# print(save)

# save = [[1,2,3,4,5,6]]

# def reset_ok():
#     global save
#     save = []

# reset_ok()
# print(save)

# lott()
# print(save)

# def lott(save):
    # save.append([1,2,3,4,5,6])


import random

def game(ranking):
    target = random.randint(1,10)
    tries = 0
    solved = False

    print("\n게임 시작! (1~10)")
    while solved == False:
        s = input("숫자 입력: ")
        if s.isdigit() == False:
            print("숫자만 입력")
        else:
            tries += 1
            guess = int(s)
            if guess < target:
                print("up")
            elif guess > target:
                print("down")
            else:
                print("정답!", tries, "회")
                name = input("이름: ")
                ranking.append([tries, name])
                ranking.sort()
                solved = True

def show_rank(ranking):
    print("\n-- 랭킹 ---")
    if len(ranking) == 0:
        print("기록 없음")
    else:
        i = 0
        r = 1
        while i < len(ranking) and i < 5:
            print(str(r) + "위", ranking[i][1], str(ranking[i][0]) + "회")
            r += 1
            i += 1
    
def main():
    ranking = []

    running = True
    while running:
        print("\n1) 게임  2)랭킹  3)종료")
        m = input("선택: ")
        if m == "1":
            game(ranking)
        elif m == "2":
            show_rank(ranking)
        elif m == "3":
            running = False
        else:
            print("1~3 중 선택")

main()