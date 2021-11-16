# 딕셔너리는 키와 값의 쌍으로 만들어지고 순서가 없으며, 수정가능, 중복 불가능
# 리터럴 생성
person = {
    'name' : '펭수',
    'age' : 30
}


# 값에 접근 방법
print(person['name'])
print(person.get('name')) # 키 값이 없더라도 에러가 나지않고 리턴 None

# 키 값을 추가하기
person['phone'] = '010-777-7777'
print(person)

# 값을 수정하기
person['name'] = '라이언'
print(person)

# 아이템 제거 (키 값과 해당 하는 값이 같이 제거)
person.pop('phone')
print(person)

