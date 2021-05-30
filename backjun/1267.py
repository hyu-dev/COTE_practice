n = int(input())
arr = list(map(int, input().split()))

def young(i):
    price = 10
    temp = int(i / 30)
    if i >= 30:
        price += (10 * temp)
    return price

def minsick(i):
    price = 15
    temp = int(i / 60)
    if i >= 60:
        price += (15 * temp)
    return price

sumY = 0
sumM = 0
for i in arr:
    sumY += young(i)
    sumM += minsick(i)

if sumY > sumM:
    print("M {0}".format(sumM))
elif sumM > sumY:
    print("Y {0}".format(sumY))
else:
    print("Y M {0}".format(sumY))