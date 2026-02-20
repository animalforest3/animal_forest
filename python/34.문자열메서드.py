text = "  Hello Python World  "
print("원본 문자열:", repr(text))
print("-" * 40)

# 1) strip / lstrip / rstrip : 공백 제거
print("strip():", repr(text.strip()))
print("lstrip():", repr(text.lstrip()))
print("rstrip():", repr(text.rstrip()))
print("-" * 40)

# 2) lower / upper / title : 대소문자 변환
print("lower():", text.lower())
print("upper():", text.upper())
print("title():", text.title())
print("-" * 40)

# 3) replace : 문자열 치환
print("replace('Python', 'AI'):", text.replace("Python", "AI"))
print("-" * 40)

# 4) split : 문자열 나누기
words = text.split()
print("split():", words)
print("-" * 40)

# 5) join : 리스트 → 문자열
joined = "-".join(words)
print("join():", joined)
print("-" * 40)

# 6) count : 특정 문자열 개수
print("count('o'):", text.count("o"))
print("-" * 40)

# 7) find / index : 위치 찾기
print("find('Python'):", text.find("Python"))
# find는 없으면 -1 반환

print("index('Python'):", text.index("Python"))
# index는 없으면 오류 발생 (ValueError)
print("-" * 40)

# 8) startswith / endswith : 시작/끝 검사
print("startswith('  Hello'):", text.startswith("  Hello"))
print("endswith('World  '):", text.endswith("World  "))
print("-" * 40)

# 9) isdigit / isalpha / isalnum : 문자열 성질 검사
s1 = "123" # True
s2 = "abc" #True
s3 = "abc123" #True

print("isdigit():", s1.isdigit()) #문자인데 숫자로만 이루어졌는지
print("isalpha():", s2.isalpha()) #문자인데 문자로만 이루어졌는지
print("isalnum():", s3.isalnum()) #문자인데 숫자+문자 되어있는지 / 공백X, 특수문자
print("-" * 40)

# 10) len : 문자열 길이
print("len(text):", len(text))
