단 = int(input("몇 단?"))

for i in range(1,단+1):
    print(2*i)

n = int(input("몇 단? : "))
for i in range(1,10):
    print(f"{n} x {i}= {n*i}")


#while문 (될 때 까지)
count = 0

while count <= 5:
    print(count)
    count += 1


num = 1
while True:
    if num == 5:
        break
    print(num)
    num += 1



    score = 50
if score > 60:
    print("합격")
else:
    print("불합격")