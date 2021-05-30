t = int(input())

def winner(x, y):
    if x == 'R':
        if y == 'P':
            return -1
        elif y == 'S':
            return 1
        else:
            return 0
    elif x == 'P':
        if y == 'S':
            return -1
        elif y == 'R':
            return 1
        else:
            return 0
    else:
        if y == 'R':
            return -1
        elif y == 'P':
            return 1
        else:
            return 0


for i in range(t):
    n = int(input())
    count = 0
    for j in range(n):
        x, y = input().split()
        count += winner(x, y)
    
    if count == 0:
        print('TIE')
    elif count > 0:
        print('Player 1')
    else:
        print('Player 2')