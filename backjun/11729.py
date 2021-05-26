n = int(input())
def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)
# 이동 횟수 공식
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
# 함수실행
hanoi(n, 1, 2, 3)
'''
맨 처음
3 1 2 3 호출 - 1단계 a
2 1 3 2 호출 - 1단계 b
1 1 2 3 호출 - 1단계 c
1 3 출력 - if n == 1
c 종료
1 2 출력 - 2단계 b
1 3 1 2 호출 - 3단계 b
3 2 출력 - if n == 1
b 종료
1 3 출력 - 2단계 a
2 2 1 3 호출 - 3단계 a
1 2 3 1 호출 - 1단계 a
2 1 출력 - if n == 1
1단계 a 종료
2 3 출력 - 3단계 a의 2단계
1 1 2 3 호출 - 3단계 a의 3단계
1 3 출력 - if n == 1
3단계 a의 3단계 종료
'''