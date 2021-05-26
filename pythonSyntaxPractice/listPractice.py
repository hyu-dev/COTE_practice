# 리스트 []

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)


# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

################## 사 전 #################
print("=====================사 전====================")
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # KeyError
# print(cabinet.get(5)) none  < 이후 코드를 이어갈 수 있음
print(cabinet.get(5, "사용가능"))

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3": "유재석", "B-100":"김태호"}
print(cabinet["A-3"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 페점
cabinet.clear()
print(cabinet)



################## 튜 플 #################
print("=====================튜 플====================")
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

################## 집 합 #################
print("=====================집 합====================")
# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# 자바를 잊었어요
java.remove("김태호")
print(java)


# 자료구조의 변경
print("=====================자료구조의 변경====================")
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


'''
Quiz)
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오

조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건 3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
 -- 당첨자 발표 --
 치킨 당첨자 : 1
 커피 당첨자 : [2, 3, 4]
 -- 축하합니다 --
'''

from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

# writer = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# winner = set(sample(writer, 4))
# coffee = set(sample(winner, 3))
# chicken = winner - coffee
# print(f"""
#  -- 당첨자 발표 --
#  치킨 당첨자 : {chicken}
#  커피 당첨자 : {coffee}
#  -- 축하합니다 --
# """)

users = range(1, 21)
# print(type(users))
users = list(users)
# print(type(users))

shuffle(users)

winners = sample(users, 4) # 4명중 하나는 치킨, 나머지는 커피
print(f"""
 -- 당첨자 발표 --
 치킨 당첨자 : {winners[0]}
 커피 당첨자 : {winners[1:]}
 -- 축하합니다 --
""")