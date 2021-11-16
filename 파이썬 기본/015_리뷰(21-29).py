# 021 while 문 실습
# while문은 조건이 참인 경우 실행문을 반복하는 반복문입니다. 
# 예제를 살펴보고 조건식의 빈칸을 올바르게 채워 보세요.

# while 3<5:         # 3<5가 참이므로
#     print("true")  # 이 코드가 반복적으로 실행됩니다.

# 문제
# 빈칸을 채워넣어 while문이 numbers의 값을 한 줄씩 출력하도록 만들어 보세요.
# ※ 빈칸은 length 변수를 이용해 채워주세요.
numbers = [1,2,3]
length = len(numbers)
i = 0
while i < length:  #코드 완성하기
    print(numbers[i])
    i = i + 1


# ​022 enumerate
# ​리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가집니다.
# enumerate는 “열거하다”라는 뜻입니다.
# 이 함수는 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아 
# 인덱스 값을 포함하는 enumerate 객체를 리턴합니다.
# # enumerate 함수
# data = enumerate([1, 2, 3])
# for i, value in data:
#     print(f"인덱스 {i}번 값은 {value}")

# 문제
# 32인 바지의 위치를 한번만 출력하고 반복문을 빠져나와야 합니다.
# break는 반복문을 종료시키는 기능을 갖고 있으므로 break를 이용하면 되겠지요.

sizes = [33,35,34,37,32,35,39,32,35,29]
for i,size in enumerate(sizes):
    if size == 32:
        print(f"사이즈 32인 바지는 {i+1}번째에 있다.")
        break


# 023 예외 try except
# ​프로그래밍을 하다 만나는 다양한 오류들은 유연하게 프로그래밍 할 수 있게 도와주는 도구가 되기도 합니다. 
# try except를 이용하면 에러의 이름을 활용하여 에러를 코드 내에서 처리할 수 있습니다.
# try:
#     # 에러가 발생할 가능성이 있는 코드
# except Exception: # 에러 종류
#     #에러가 발생 했을 경우 처리할 코드

# 문제
# 다음 코드는 3을 0으로 나누고 있습니다. 
# 나눗셈 연산은 0으로 나눌 수 없기 때문에 문제의 코드를 실행하면 에러가 발생합니다. 
# 에러의 이름을 확인하고 try except문으로  줄을 감싸서 에러가 발생할 경우 
# print문이 출력되도록 만들어 보세요.
try :
    a = 3/0
except :
    print("0으로 나눌 수 없습니다.")


# ​024 예외의 이름을 알고싶을때
# 예외의 이름을 모르는 경우에는 Exception as를 통해 해결할 수 있습니다.
# try:
#     # 에러가 발생할 가능성이 있는 코드
# except Exception as ex:     # 에러 종류
#     print('에러가 발생 했습니다', ex)  # ex는 발생한 에러의 이름을 받아오는 변수

# 문제
# 다음 코드는 발생하는 예외를 try/except문으로 처리하고 있습니다. 
# 어떤 에러가 발생하는지 출력할 수 있도록 빈칸을 채우고, 
# 예외를 출력할 수 있도록 format의 빈칸을 작성하세요.
try:
    a = 5
    b = 0
    c = a / b
except Exception as ex:
    print(f'다음과 같은 에러가 발생했습니다: {ex}')


# ​025 bool 논리연산
# ​true와 false 논리연산은 아래와 같이 이루어 질 수도 있습니다.
# 문제
# 다음중 어떤 if 코드가 실행되는지 확인하시오.
if []:
    print("[]은 True입니다.")
if [1, 2, 3]:
    print("[1,2,3]은/는 True입니다.")
if {}:
    print("{}은 True입니다.")
if {'abc': 1}:
    print("{'abc':1}은 True입니다.")
if 0:
    print("0은/는 True입니다.")
if 1:
    print("1은 True입니다.")


# ​026 논리연산자 or
# a = True or 1      #True   앞의 값이 True입니다.
# b = False or 0     #0      앞의 값이 False이므로 뒤의 값을 따릅니다.
# c = 0 or False     #False  앞의 값이 0이므로 False입니다. 따라서 뒤의 값인 False를 따릅니다.
# d = 1 or False     #1      앞의 값이 1이므로 True입니다.

# 문제
# ​or연산의 결과는 앞의 값이 True이면 앞의 값을, 
# 앞의 값이 False이면 뒤의 값을 따릅니다. 
# 다음 코드를 실행해서 각각 a와 b에 어떤 값이 들어가는지 확인해 보세요.
a = 1 or 10    # 1의 bool 값은 True입니다.
b = 0 or 10    # 0의 bool 값은 False입니다.
print(f"a:{a}, b:{b}")


# ​027 리스트 실습
# list.insert(index, value) : 원하는 위치에 값을 추가합니다

# list = [1, 2, 3]
# list.insert(3, 4)     #list = [1, 2, 3, 4]로 4가 추가되었습니다.
# list.sort() : 값을 순서대로 정렬

# list = [3, 5, 6, 4, 2, 1]
# list.sort()           #list = [1, 2, 3, 4, 5, 6]으로 정렬됩니다.
# list.reverse() : 값을 역순으로 정렬

# list = [3, 5, 6, 4, 2, 1]
# list.reverse()     #list = [1, 2, 4, 6, 5, 3] 역순으로 정렬됩니다.

# 문제
list1 = [1, 2, 3, 4]
# 아래줄에서 list1의 1번째 자리에 8을 넣고 원래 있던 값은 오른쪽으로 밀어 보세요.
list1.insert(1,8)
print("첫 번째 자리에 8을 넣은 결과 : {}".format(list1))

# 아래줄에서 list1을 작은 수부터 큰 수로 정렬해 보세요
list1.sort()
print("list1을 작은 수부터 큰 수로 정렬한 결과 : {}".format(list1))

# 아래줄에서 list1을 거꾸로 만들어 보세요
list1.reverse()
print("list1을 거꾸로 정렬한 결과 : {}".format(list1))


# ​028 문자열과 리스트
# List와 String의 유사성을 이용해 보세요.
# 리스트와 문자열은 서로 변환할 수 있습니다.
# 예를 들어,
str = "10:35:27"
list = str.split(":")             #문자열을 ":"기준으로 리스트화
new_str = ":".join(list)          #리스트를 ":"기준으로 문자열화

# 문제
# 다음 코드는 "오늘은 날씨가 흐림"이라는 문자열을 "오늘은 날씨가 맑음"이라는 
# 문자열로 바꾸는 과정을 보여주고 있습니다. 
# 코드의 안내를 따라 빈 부분을 작성해 보세요.
str = "오늘은 날씨가 흐림"
# split()을 이용해서 str을 공백으로 나눈 문자열을 words에 저장하세요
words = str.split()

# index()를 이용해서 "흐림"이 words의 몇번째에 있는지 찾고, 
# position에 저장하세요.
position = words.index('흐림')
words[position] = "맑음"  #흐림을 맑음으로 수정

# join()을 이용해서 words를 다시 문자열로 바꿔 new_str에 저장하세요. 
# words를 문자열로 바꿀때는 공백 한 칸을 기준으로 붙이면 됩니다.
new_str = ' '.join(words)

print(new_str)


# ​039 리스트 slice
# Slicing
# 리스트나 문자열에서 여러개의 값을 가져오는 기능입니다.
# 예를 들어,
text = "hello world"
text[1:5]         # ello          1번째부터 5번째 전까지
text[3:]          # lo world      3번째부터 끝까지
text[:3]          # hel           처음부터 3번째까지
text[:]           # hello world   처음부터 끝까지

# 문제
rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
# red_colors가 ["빨", "주", "노"]의 값을 가지도록 rainbow를 slice하세요.
red_colors = rainbow[0:3]

#blue_colors가 ["파", "남", "보"]의 값을 가지도록 rainbow를 slice하세요.
blue_colors = rainbow[4:7]

print("red_colors의 값 : {}".format(red_colors))
print("blue_colors의 값 : {}".format(blue_colors))