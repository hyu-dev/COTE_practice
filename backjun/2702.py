# n = int(input())

# arr = { 'maxNum': 1, 'minNum': 2}

# def test(a, b, j):
#     if isinstance(a / j, int) or isinstance(b / j, int):
#         arr['maxNum'] *= (a * b)
#         return
#     else:
#         arr['maxNum'] *= j
#         arr['minNum'] *= j
#         a = a // j
#         b = b // j
#         return test(a, b, j)

# temp = 0
# for i in range(n):
#     a, b = map(int, input().split())
#     temp = min(a, b)
#     for j in range(2, temp+1):
#         test(a, b, j)


def gcd(a, b):
    print("시작 : ",a,b)
    while b is not 0:
        d = a % b
        a = b
        b = d
        print("종료 : ", a, b)
    return a

def _2702():
    T = int(input())
    for i in range(T):
        A, B = map(int, input().split(' '))
        print((A * B) // gcd(B, A), gcd(B, A))

_2702()
            