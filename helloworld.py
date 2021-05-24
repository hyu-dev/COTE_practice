def solution(places):
    result = []
    for i in places:
        flag = "1"
        for j in range(0, 5):
            for k in range(0, 5):
                print(j, k)
                if i[j][k] == "P" and k < 3 and i[j][k+2] == "P" and i[j][k+1] != "X":
                    print("1번에서 걸림")
                    result.append(0)
                    flag = "2"
                elif i[j][k] == "P" and j < 3 and i[j+2][k] == "P" and i[j+1][k] != "X":
                    print("2번에서 걸림")
                    result.append(0)
                    flag = "2"
                elif i[j][k] == "P" and k < 4 and i[j][k+1] == "P":
                    print("3번에서 걸림")
                    result.append(0)
                    flag = "2"
                elif i[j][k] == "P" and j < 4 and i[j+1][k] == "P":
                    print("4번에서 걸림")
                    result.append(0)
                    flag = "2"
                elif i[j][k] == "P" and k < 4 and j < 4 and i[j+1][k+1] == "P" and (i[j][k+1] != "X" or i[j+1][k] != "X"):
                    print("5번에서 걸림")
                    result.append(0)
                    flag = "2"
                elif i[j][k] == "P" and 0 < k < 4 and 0 < j and i[j-1][k-1] == "P" and (i[j][k+1] != "X" or i[j-1][k] != "X"):
                    print("6번에서 걸림")
                    result.append(0)
                    flag = "2"
            if flag == "2":
                break;
        if flag == "1":
            result.append(1)
            print("다음!")
    
    return result

test = solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
print(test)