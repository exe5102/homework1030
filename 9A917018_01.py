quantity = int(input("請輸入星星數量:"))
j = -1
for i in range(round(quantity/2), 0, -1): #只做上三角
    j += 2
    print(" "* i + "*"* j)

print("*" * quantity)                     #分界線

for i in range(1, round(quantity/2)+1, 1): #只做下三角
    print(" "* i + "*"* j)
    j -= 2