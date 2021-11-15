# f - string
name = '홍길동'
age = 20
print(f'안녕하세요 {name}님 나이가 {age}살 이군요')

# 2. 문자열.format()
welcome = '환영합니다'
number = 20
print('{}번 손님 {}'.format(number, welcome))

# 예제 1
# 변수 name과 color에 자신의 이름과 좋아하는 색상을 문자열로 입력하고 
# .format()방법과 f-string 방법으로 괄호 안을 수정해서 자신의 이름과 좋아하는 색상을 출력해 보세요. ( 두가지 방법을 다 사용해 보세요)

name = '박성민'
color = '흰색'
print('안녕하세요. 제 이름은 {}이고 좋아하는 색상은 {}입니다.'.format(name, color))
print(f'안녕하세요. 제 이름은 {name}이고 좋아하는 색상은 {color}입니다.')


# 문자열 인덱스 : 문자열은 인덱스 번호를 사용가능
string1 = 'abcdefg'

# 문자열[인덱스번호]
print(string1[2]) # 0부터 시작해서 2번자리 c가 출력

# 문자열 슬라이싱 [시작:끝]  (시작은 포함, 끝은 포함안됨)
print(string1[0:4]) # 0번 a부터 시작해서 4번 e앞까지 d까지 출력

# 문자열 역순 출력 [시작:끝:증감]
print(string1[::-1])
print(string1[6:3:-1])

# 인덱스 번호로 값을 출력 가능하지만, 부분적으로 수정 불가


# 예제 1. 두 자리 숫자 입력 후 각 자리 숫자 더하기
# 🚨 이 부분은 고치지 마세요 👇
two_digit_number = input("두 자리 숫자를 입력: \n")
# 🚨 이 부분은 고치지 마세요 👆

####################################
# 아래에 코드를 작성합니다. 👇
a = int(two_digit_number)
b = (a//10) + (a%10)
c = str(b)
print('두 숫자의 합은 ' + c + ' 입니다' )

x = two_digit_number[0]
y = two_digit_number[1]
z = int(x) + int(y)
print(f'{x} + {y} = {z}')


# 예제 2. BMI 지수 계산기
# 🚨 여기는 그대로 👇
height = input("키를 미터 단위로 입력하세요 : ")
weight = input("몸무게를 킬로 단위로 입력하세요 : ")
# 🚨 여기는 그대로 👆

#아래에 코드 작성 👇
BMI = float(weight) / float(height)**2
print(f'당신의 bmi 지수는 {round(BMI,2)} 입니다.')
