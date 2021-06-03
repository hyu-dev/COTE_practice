n = int(input())
array = list(map(int, input().split()))

seat = {}
sumNum = 0
for i in array:
    if i in seat:
        sumNum += 1
    else:
        seat[i] = 1

print(sumNum)