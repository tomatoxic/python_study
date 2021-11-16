# ​011 딕셔너리 삭제하기
# 아래의 예 처럼 딕셔너리를 수정할 수 있습니다.
# dict['one' : 1, 'two' : 2]
# dict['three'] = 3    # 값을 추가합니다  {'one' : 1, 'two' : 2, 'three' : 3}
# dict['one'] = 11     # 값을 수정합니다  {'one' : 11, 'two' : 2, 'three' : 3}
# del(dict['one'])     # 값을 삭제합니다  {'two' : 2, 'three' : 3}
# dict.pop('two')      # 값을 삭제합니다  {'three' : 3}

# 문제
# days_in_month에는 엉뚱하게도 -1월이라는 이름표와 값이 있는데요. 
# 이 값을 지워보세요.
days_in_month = {"1월":31, "2월":28, "3월":31,"-1월":97889789}
del(days_in_month['-1월'])
print(days_in_month)
 

# ​012  딕셔너리와 반복문
# ​딕셔너리를 반복문에서 활용하는 방법을 알아봅시다. 
# 딕셔너리의 반복문에서는 경우에 따라 key를 가져올 수도 있고 
# 값을 가져올 수도 있습니다. 아래의 예를 참고하여 문제를 해결해 보세요.
# ages = {'Tod' : 35, 'Jane' : 23, 'Paul' : 62}
# for key in ages.keys():      # keys() 생략 가능
#     print(key)               # Tod, Jame, Paul이 출력됩니다.
# for value in ages.values():
#     print(value)             # 62, 23, 35가 출력됩니다.

# 문제
# for in문을 이용해서 days_in_month2의 이름표(key)를 한줄씩 출력해 보세요.
days_in_month2 = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}
for n in days_in_month2.keys():
    print(n)


# ​013 문자열 출력
# 딕셔너리의 반복문에서는 key와 value를 선택해서 가져올 수 있었지요. 
# 이번 문제처럼 key와 value를 둘 다 가져와야 할 때에는 
# items()를 사용하면 됩니다. 아래의 예를 참고하여 문제를 해결해 보세요.
# ages = {'Tod' : 35, 'Jane' : 23, 'Paul' : 62}
# for key, value in ages.items():
#     print(f'{key}의 나이는 {value} 입니다')

# 문제
# days_in_month의 각 이름표와 값을 다음과 같은 형식으로 출력해 보세요.
days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}
for key,value in days_in_month.items():
    print(f'{key}에는 {value}일이 있습니다.')


# ​014 random 실습
# 문제
# https://docs.python.org/3.5/library/random.html#random.choice 
# 에서 random.choice의 활용법을 확인하고, 
# random_element가 list의 element중 하나를 가지도록 만들어 보세요.

import random
list = ["빨","주","노","초","파","남","보"]
random_element = random.choice(list)
print(random_element)


# ​​015 random 실습
# 문제
# https://docs.python.org/3/library/random.html?highlight=random.randint#random.randint 
# 에서 random.randint의 활용법을 확인하고, 
# random_number가 2보다 크거나 같고, 5보다 작거나 같은 임의의 정수를 가지도록 만들어 보세요.
import random
random_number = random.randint(2,5)
print(random_number)


# ​016 문자열 출력하기
# 문제
# https://docs.python.org/3.5/library/random.html#random.shuffle 
# 에서 random.shuffle의 활용법을 확인하고, 
# random.shuffle()을 활용해서 list의 순서를 섞어 보세요. 

import random
list = ["빨","주","노","초","파","남","보"]
# 여기에 코드를 작성해 보세요.
random.shuffle(list)
print(list)


# ​017 datetime 실습
# 파이썬의 날짜모듈을 이용한 문제입니다. 
# 모듈 사용법을 알아보기 위해 검색을 해보세요. 
# 검색은 구글을 이용하며, '파이썬3' 또는 'python3' 키워드가 
# 포함된 단어를 입력하여 원하는 정보를 검색합니다.
# datetime모듈에 대해 검색하고 문제를 해결해 보세요.

# 문제
# 첫줄의 빈칸에 datetime모듈을 import하고, 
# 두번째 줄의 print문의 괄호 안에 
# datetime.date.today()를 입력해서 오늘 날짜를 출력해 보세요.
import datetime
print(datetime.date.today())


# ​018 문자열 실습
# 줄 바꿈과 따옴표, 큰 따옴표 모두 섞어 써야하는 문장이므로
# 따옴표/큰따옴표 3개를 이용하면 쉽게 풀 수 있어요.
# string = """줄도 바꿀 수 있고
# 큰따옴표"와 따옴표'를
# 마음대로 쓸 수 있습니다."""

# 문제
# 다음과 같은 문자열을 값으로 가지는 변수 string1을 선언하세요.
string1 = '''
다스베이더가 말했다.
"내가 니 애비다!"
그 말을 들은 루크는 '깜짝' 놀랐다.
'''
# list1 에 string1의 문자열을 단어로 분리하여 리스트로 만들어 입력하세요.
# list1의 5번째 요소인 list1[4] 를 출력하시오.
list1 = string1.split()
print(list1[4])


# 019 반복문 사용하기
# 순회할 리스트가 정해져 있고, 그 리스트에서 하나씩 꺼내 쓰기만 되는 상황이라면 
# for in list를, 순회할 횟수가 정해져 있거나 1씩 증가하는 숫자가 필요하다면
# for in range()를 사용하는 것이 좋습니다.
# 문제
# days에는 1월부터 12월까지 그 달에 포함된 날짜수가 정리되어 있습니다.
# 다음과 같이 출력되도록 for in문을 만들어 보세요.
days = [31,29,31,30,31,30,31,31,30,31,30,31]
for i in range(len(days)) :
     print(f'{i+1}월의 날짜수는 {days[i]}일 입니다.')


# ​020 정수와 실수
# ​a를 b로 나눈 몫을 값으로 가지므로
# /연산자가 아닌 //연산자를 사용해야 합니다.
# 예를 들어,
# div1 = 6 / 5    # div = 1.2
# div2 = 6 // 5   # div = 1

# 문제
# 변수 div를 선언하고, 변수 a를 b로 나눈 몫을 값으로 가지도록 계산해 보세요.
a=23
b=5
div = a // b
print(f"a를 b로 나눈 몫은 {div}입니다.")