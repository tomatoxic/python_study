# 튜플(tuple)은 순서가 있고 수정불가인 자료구조, 중복 가능
# 리스트와 다른점은 수정 불가, 표시는 () 괄호

# 튜플을 리터럴로 만들기
fruit_tuple = ('사과','오렌지','망고')

# 값을 가져오기
print(fruit_tuple[1])

# 값은 수정 불가
# fruit_tuple[1] = '포도'

# 길이 (아이템 개수)
print(len(fruit_tuple))

# 튜플의 삭제
# del fruit_tuple # 전체 삭제
# print(fruit_tuple) # 없으므로 에러발생


# SET 자료형
# set은 순서(인덱스)가 없고 중복 불가능
# 표시는 {}
fruit_set = {'사과','오렌지','망고'}

# set에 있는지 없는지 검사
print('사과' in fruit_set) # 사과가 fruit_set에 있으므로 true

# set에 추가 add
fruit_set.add('포도')
fruit_set.add('포도')
fruit_set.add('포도')
fruit_set.add('사과')
fruit_set.add('사과')
print(fruit_set)

# set에서 제거
fruit_set.remove('포도')

# 클리어 set
fruit_set.clear() # 모든 아이템 삭제
print(fruit_set)

