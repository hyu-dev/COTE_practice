def solution(n):
    s = fibonacci(n)
    div = s / 1234567
    return s

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
