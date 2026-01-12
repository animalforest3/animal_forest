#라이브러리_기초
import math #수학 내장/내부 라이브러리

print("pi =", math.pi)
print("sqrt(25) =", math.sqrt(25))
print("pow(2, 10) =", math.pow(2, 10))
print("ceil(3.14) =", math.ceil(3.14))
print("floor(3.99) =", math.floor(3.99))



import random

random.seed(42)

nums = [1, 2, 3, 4, 5]
print("원본:", nums)

# 1) random(): 0.0 ~ 1.0
print("random() =", random.random())

# 2) randint(a, b): a ~ b (양끝 포함)
print("randint(1, 10) =", random.randint(1, 10))

# 3) randrange(start, stop, step): stop 미포함
print("randrange(0, 10, 2) =", random.randrange(0, 10, 2))

# 4) choice(리스트): 하나 뽑기
print("choice(nums) =", random.choice(nums))

# 5) choices(리스트, k=N): 복원추출(중복 가능)
print("choices(nums, k=3) =", random.choices(nums, k=3))

# 6) sample(리스트, k=N): 비복원추출(중복 불가)
print("sample(nums, k=3) =", random.sample(nums, k=3))

# 7) shuffle(리스트): 원본 자체를 섞음(리턴값 None)
random.shuffle(nums)
print("shuffle 후:", nums)



import os

BASE_DIR = "demo_os"
os.makedirs(BASE_DIR, exist_ok=True)  # 이미 있으면 에러 없이 통과
print("폴더 생성/확인:", os.path.abspath(BASE_DIR))



import os

path = os.path.join("demo_os", "hello.txt")

# 파일 쓰기(없으면 자동 생성)
with open(path, "w", encoding="utf-8") as f:
    f.write("Hello!\n")
    f.write("파일이 생성되었습니다.\n")

print("파일 생성:", os.path.abspath(path))

# 파일 읽기
with open(path, "r", encoding="utf-8") as f:
    print("---- 파일 내용 ----")
    print(f.read())



import os

files = os.listdir("demo_os")
print("demo_os 안의 목록:", files)



import os

target = os.path.join("demo_os", "hello_renamed.txt")

if os.path.exists(target):
    os.remove(target)
    print("파일 삭제 완료:", target)
else:
    print("삭제할 파일이 없음:", target)



import os

# 폴더가 비어있어야 삭제 가능
if os.path.exists("demo_os") and len(os.listdir("demo_os")) == 0:
    os.rmdir("demo_os")
    print("폴더 삭제 완료: demo_os")
else:
    print("폴더가 없거나, 비어있지 않아서 삭제 불가")

# 폴더 안에 남아 있어도 강제로 삭제
import shutil

if os.path.exists("demo_os"):
    shutil.rmtree("demo_os")
    print("폴더 전체 삭제 완료: demo_os")



import datetime

# 고정된 시간(결과 일정하게)
dt = datetime.datetime(2026, 1, 4, 9, 30, 15)

print("datetime:", dt)
print("year:", dt.year, "month:", dt.month, "day:", dt.day)
print("weekday(월0~일6):", dt.weekday())
print("포맷:", dt.strftime("%Y-%m-%d %H:%M:%S"))



import datetime
import os

now = datetime.datetime.now()
stamp = now.strftime("%Y%m%d_%H%M%S")  # 20260104_093015 같은 형태

folder = "logs"
os.makedirs(folder, exist_ok=True)

filename = f"log_{stamp}.txt"
path = os.path.join(folder, filename)

with open(path, "w", encoding="utf-8") as f:
    f.write(f"생성 시각: {now}\n")
    f.write("로그 시작!\n")

print("로그 파일 생성:", os.path.abspath(path))



import os
import datetime

today = datetime.date.today().strftime("%Y-%m-%d")
folder = os.path.join("reports", today)
os.makedirs(folder, exist_ok=True)

path = os.path.join(folder, "result.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write("오늘의 결과 파일\n")

print("저장 위치:", os.path.abspath(path))