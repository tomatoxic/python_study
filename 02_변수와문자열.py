# 여러개의 변수를 동시에 초기화
a, b, c = 1, 2, 3
print(a, b, c)

# 예제 2
# print( ) 출력 함수를 이용하여 x변수에 값 10을 저장하고 출력
x = 10
print(x)

# 예제 3
# 여러개의 변수 x, y, z 에 각각 1 , 2, 3 을 저장하고 출력하라
x, y, z = 1, 2, 3
print(x, y, z)

# 예제 4
# 결과가 <class 'int'> <class 'float'> <class 'str'> 같이 나오도록
# x,y,z 값에 정수, 소수, 문자열을 입력하여 그 타입(Type)을 출력
x = 1
y = 1.1
z = '일점일'
print(type(x))
print(type(y))
print(type(z))

# 예제 5 아래와 같이 a와 b에 값을 입력하면 a, b값이 바뀌어서 출력된다.

# 입력
# a: 3
# b: 5
# 출력
# a: 5
# b: 3
a = input('a : ')
b = input('b : ')
print('a : ' + b)
print('b : ' + a)