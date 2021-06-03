n, k = map(int, input().split())

arr = []
for i in range(2, n+1):
    if n % i == 0 and n // i != 1:
        arr.append([i, n//i])

flag = False
temp = 0
if arr[0][0] < k and arr[0][1] < k:
    flag = True
    temp = min(arr[0][0], arr[0][1])
elif arr[0][0] < k or arr[0][1] < k:
    flag = True
    temp = min(arr[0][0], arr[0][1])

if flag:
    print("BAD", temp)
else:
    print("GOOD")



# p, k = map(int, input().split())

# # pas = p * q
# # 에리토스테네스의 체 -> 소수 구하기
# prime = [False, False] + [True]*(p-2)
# print(prime)
# # print(int(k**0.5)+1)   # 4
# for i in range(2, int(k**0.5)+1):
#     # print(i) # 2 3
#     # print(prime[i]) # True True
#     if prime[i]:
#         #print(i+i) # 4 6
#         for j in range(i+i, k, i): # 4 11 2  / # 6 11 3
#             # print(j) # 4 6 8 10 / # 6 9
#             if prime[j]:
#                 prime[j] = False

# flag = True
# for i in range(2,k):
#     if prime[i]:
#         # print(prime[i]) # True True True True
#         if p % i == 0:
#             flag == False
#             break

# if flag:
#     print('GOOD')
# else:
#     print('BAD', i)