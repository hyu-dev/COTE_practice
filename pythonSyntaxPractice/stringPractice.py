# 애완동물을 소개해주세요
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name, "는 ", age, "살이며, ", hobby,"을 아주 좋아해요")
#print(name + "는 어른일까요? " + is_adult)
print(name + "는 어른일까요? " + str(is_adult))
# 프린트시 정수형이나 불린형은 str로 씌워주어 출력해야 에러가 안난다

''' 여러문장을 주석처리
하고 싶다면
작은 따옴표를
3개 이용한다
'''

'''
컨트롤 + 슬래시를 입력하면
한번에 주석을 할 수 있다
해제 또한 마찬가지
'''

'''
Quiz) 변수를 이용하여 다음 문장을 출력하시오

변수명
 : station

변수값
 : "사당", "신도림", "인천공항" 순서대로 입력

출력 문장
 : xx 행 열차가 들어오고 있습니다.
'''

station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")

print(2**3) # 2^3 = 8
print(5%3) #나머지 구하기 2
print(5//3) #몫 구하기 1

print(3 == 3)   # True

print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5)) #True

print((3 > 0) or (3 > 5)) #True
print((3 > 0) | (3 > 5)) #True
print(5 > 4 > 3) #True
print(5 > 4 > 7) #False

print("===========================")
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 5
print(number)
print("===========================")
print(abs(-5)) # 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

print("===========================")
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(int(random() * 45) + 1)
print(randrange(1, 46)) # 1~ 46 미만의 임의이 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

'''
Quiz)
당신은 최근에 코딩 스터디 모이을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오

조건 1 : 랜덤으로 날짜를 뽑아야 함
조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28일내로 정함
조건 3 : 매월 1 ~ 3일은 스터디 준비를 해야하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''
print("오프라인 스터디 모임 날짜는 매월 " + str(randint(4, 28))  + "일로 선정되었습니다.")

print("===========================")
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

print("===========================")
jumin = "991212-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지
print("월 : " + jumin[2:4]) 
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

print("===========================")
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[1].isupper())
print(len(python)) # 문자열의 길이
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # -1
#print(python.index("Java")) 에러
print(python.count("n"))

password = "http://google.com"
index = password.index(".")
password = password[7:index]
result = password[:3] + str(len(password)) + str(password.count("e")) + "!"
print(f"생성된 비밀번호 : {result}")