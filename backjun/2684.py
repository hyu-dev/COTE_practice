n = int(input())

for i in range(n):
    case = input()
    arr = [0]*8
    for j in range(len(case)):
        if j > 1:
            text = case[j-2] + case[j-1] + case[j]
            if text == 'TTT':
                arr[0] += 1
            elif text == 'TTH':
                arr[1] += 1
            elif text == 'THT':
                arr[2] += 1
            elif text == 'THH':
                arr[3] += 1
            elif text == 'HTT':
                arr[4] += 1
            elif text == 'HTH':
                arr[5] += 1
            elif text == 'HHT':
                arr[6] += 1
            elif text == 'HHH':
                arr[7] += 1
    print(' '.join(map(str, arr)))