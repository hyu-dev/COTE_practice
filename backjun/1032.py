n = int(input())

array = []
for i in range(n):
    text = input()
    for j in range(len(text)):
        if len(array) < len(text):
            array.append(text[j])
        else:
            if array[j] != text[j]:
                array[j] = '?'

for i in array:
    print(i, end="")