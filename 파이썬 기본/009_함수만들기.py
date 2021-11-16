# def 함수이름(인자1,....)
def hello():
    print('하이!')
    print('안녕!')
    print('니 하오!')

# hello() # 함수 호출


# 매개변수 (파라미터, 인수) 있는 함수
def hello(name):
    print('하이 ' + name)

# hello('성민')
# hello('펭수')


def add10(num): 
  return num + 10
# print(add10(1))
# print(add10(2))


# 예제 1 ) 숫자를 입력받아서  홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(num):
    if num % 2 == 0:
        print('짝수')
    else :
        print('홀수')
is_odd(3)


# 예제 2 ) 입력으로 들어오는 모든 수의 평균 값을 계산해 리턴하는 함수를 작성해 보자. 
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다. => 매개변수 앞에 * 붙인다.)
# ex) def foo(*arg): => arg 매개변수는 가변갯수
# sum() => 합계
# ※ 평균 값을 구할 때 len 함수를 사용해 보자.

# print(avgNums(1, 2, 3)) ==> 2.0
# print(avgNums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) ==> 5.5


def avgNums(*n): # *은 가변 매개변수
    return sum(n)/len(n)

print(avgNums(1,2,3,4,5,6,7,8))
