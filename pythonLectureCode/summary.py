# 함수 정의 및 람다(lambda) 사용
""" 
- 함수 선언
def 함수명(parameter):
    code


- 함수 다양한 사용
- 다양한 반환 값
- *args, **kwargs
- 람다 함수
"""

# 함수 선언 위치 중요

# 예제 1
def hello(world):
    print("Hello", world)

hello('Python!')
hello(777)

# 예제 2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!!")
print(str)

# 예제 3 (다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 예제 3 (데이터 타입 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3)

lt = func_mul2(100)
print(lt, type(lt))

# 예제 4
# *args, *kwargs

def args_func(*args):
    # print(type(args), args)
    # for i,v in enumerate(args):
    #     print(i, v)
    for i,v in enumerate(range(10)):
        print(i, v)

args_func('kim')
args_func('kim', 'Park')
args_func('kim', 'Park', 'Lee')

# kwargs
def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(kwargs)

kwargs_func(name1='Kim', name2='Park', name3='Lee')

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)

# 예제 5
# 중첩함수(클로저)
# decorator
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 1000)

nested_func(1000)

# 예제 6 (hint)
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3)

print(func_mul3(5))

# 람다식 예제
"""
- 람다식 : 메모리 절약, 가독성 향상, 코드 간결
- 함수는 객체 생성 -> 리소스(메모리) 할당
- 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화
"""

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)
print(var_func(10))

lambda_mul_10 = lambda num: num * 10

print(lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x : x * 1000))


"""
클래스 선언 및 Self 의 이해

** 클래스, 인스턴스 차이 중요
** 네임스페이스 : 객체를 인스턴스화 할 떄 저장된 공간
** 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
** 인스턴스 변수 : 객체마다 별도 존재

- 클래스 선언
class 클래스명:
    함수
    함수
    함수

- 클래스 네임스페이스 Self
- 클래스, 인스턴스 변수
- Self


클래스 상송, 다중 상속
- 클래스 상속
- 클래스 상속 예제 코드
- 클래스 다중 상속
"""

# 선언
# 예제 1
class UserInfo:
    # 속성, 메소드
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)

# 네임스페이스
user1 = UserInfo("Kim")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# 예제 2
# self의 이해
class SelfTest:
    def function1():
        print('function1 called!')
    def function2(self):
        print('function2 called!')

# self_test = SelfTest()
# self_test.function1()

class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)


# 상속, 다중상속
# 예제 1
# 상속 기본
# 슈퍼클래스(부모) 및 서비클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모
class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color
    
    def show(self):
        return 'Car Class "show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name
    
    def show(self):
        print(super().show())
        return "Car Info : %s %s %s" % (self.car_name, self.type, self.color)


# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__)

# Method Overriding(오버라이딩)
model2 = BenzCar("220d", "suv", "black")
print(model2.show())

# Parent Method Call
model3 = BenzCar("350s", 'sedan', 'silver')
print(model3.show())

# Inheritance Info(상속 정보 리스트 타입으로 반환)
print(BmwCar.mro())
print(BenzCar.mro())

# 예제 2
# 다중 상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
print(A.mro())