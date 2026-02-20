# #한 줄 씩 실행해야 오류가 안남
# n = int(input("몇 단? : "))
# for i in range(1,10):
#     print(f"{n} x {i}= {n*i}")

#     for i in range(1, 2):
#     print("*" * i)
# for i in range(1, 3):
#     print("*" * i)
# for i in range(1, 4):
#     print("*" * i)

# for k in range(2,5):
#     for i in range(1, k):
#         print("*" * i)

# #중첩 for문
# for dan in range(2,5):
#     print(f"{dan}단")
#     for num in range(1,10):
#         print(f"{dan} x {num} = {dan * num}")



# #별찍기 for문
# n = int(input("몇 층 찍을까요? : "))
# for i in range(1, n + 1):
#     print("*" * i)
    
# n = int(input("몇 층 찍을까요? : "))
# for i in range(n, 0, -1):
#     print(" " * (n - i) + "*" * i)

# n = int(input("몇 층 찍을까요? : "))
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))


#별찍기 중첩for
# n = int(input("몇 층 찍을까요? :"))
# for i in range(1,n+1):
#     for j in range(1, n+2):
#         if i == j:
#             print("*" * j)


#별찍기 중첩for 거꾸로 왼쪽
# n = int(input("몇 층 찍을까요? :"))
# for i in range(1, n+1):
#     for j in range(n-i+1):
#         print("*", end="")
#     print()


# 별찍기 중첩for 거꾸로 오른쪽
# n = int(input("몇 층 찍을까요? :"))
# for i in range(1, n+1):
#     for j in range(i):
#         print(" ", end="")

#     for j in range(n-i+1):
#         print("*", end="")
#     print()


# 별찍기 트리
# for i in range(top):
#     print(' ' *(top-i-1), end="")
#     for n in range(1, i*2+2):
#         print('*', end="")
#     print()