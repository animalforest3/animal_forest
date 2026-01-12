# 리스트 1차원 2차원
# 딕셔너리
person = {"name1":"이서진","age":24,"s":[1,2,3]}    #이름:값 키:값
print(person)
print(type(person["name1"]))
student = {"name":"이서진","age":24,"grade":4}
print("이름",student["name"])

person["name1"] = "이서현"
person["이름"] = "이서현"
person["age"] = "28"
print(person)

for k in person:
    print(k)    #key
    print(person[k])    #value

#여러 학생 정보 관리
students = [
    {"name":"민수","score":80},
    {"name":"노수","score":70},
    {"name":"영수","score":60}
]
for s in students:
    print(s["name":, s["score"]])
total = 0
for s in students: # 리스트 반복문
    total += s["score"]
print("평균 점수 :", total/len(students))
student = {"name":"이서진","age":24,"grade":4}
if student["grade"] >= 3:
    student["age"] = "우수 학생"
else:
    student["result"] = "보통 학생"
print(student)
student = {"name":"이서진","age":24,"grade":4}
print(person.keys())
print(person.values())
print(person.items())

for k, v in person.items(): #('name1', '이서진')
    print(k,v)

#딕셔너리 메서드
#값 가져오기
print(person.get("age"))
print(person.get("name1"))
#값 추가/갱신
print(person.update({"age":22,"city":"seoul"}))
print(person)
#값 삭제1
a = person.pop("s")
print(a)
print(person)
#값 삭제2 - 완전 삭제
del person["이름"]
print(person)

#마지막 요소 삭제 = popitem()
k,v = person.popitem
print(k,v)
print(person)
# #전체 삭제 clear()
# person.clear()
print(person)
print(len(person))  #정수로 반환
#포함 여부 (키 기준) in
print("name1" in person)
print("age" in person)