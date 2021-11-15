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


# 문자열
# 긴 문자열은 따옴표 3개 (''' 또는 """")
var3 = '''
따옴표3개는
끝나는 문장
모두를 처리
-----------
'''
print(var3)

# 문자열 연산
성 = '홍'
이름 = "길동"
name = 성 +' '+이름
print(name)

# 타입 변환 str( ), int( ) , float( ) ...

print(type(int(str(100))))
a = str(100)
b = int(a)
c = type(b)
print(c)


# 예제 1
# 아래와 같이 출력 되도록 변수 날씨에 이스케이프 문자들을 추가하여 만들어라.
날씨 = '\tIt\'s "kind of" sunny\nHave a nice Day!'
print(날씨)

# 예제 2
# 다음과 같은 문단을 문자열을 값으로 가지는 변수 string1을 선언하세요.

# 다스베이더가 말했다.
#  "내가 니 애비다!" 
# 그 말을 들은 루크는 '깜짝' 놀랐다.

# string1을 선언하세요.
string1 = '''
다스베이더가 말했다.
"내가 니 애비다!"
그 말을 들은 루크는 '깜짝' 놀랐다.
'''
print(string1)


# 예제 3
# 밴드 이름 만들기 아래처럼 프로그램을 만듭니다. 아래 깃허브 코드를 참고
# https://github.com/jbkim08/python_lesson/blob/main/Ex1-2
print('밴드 이름 만들기 프로그램입니다.')
city = input('태어난 도시가 어딘가요?\n')
pet = input('당신의 애완동물은?\n')
band = print('당신의 밴드 이름은 ' + city + ' ' + pet)

