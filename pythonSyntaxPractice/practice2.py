# 분기
# weather = input("오늘 날씨는 어때요? ")

# if weather == "비" or weather == "눈": 
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")


# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

absend = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absend:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))


# 출석번호가 1,2,3,4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)


from random import *
count = 0;
for i in range(1, 51) :
    time = randint(5, 50);
    if time <= 15 :
        print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format("0", i, time))
        count += 1
    else:
        print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(" ", i, time))


print(f"총 탑승 승객 : {count} 분")