# if 문 문법
# a, b = 10, 10
# if a > b:
#     print("조건이 참이면 실행")
#     print("실행코드는 뛰어쓰기로 구분")
#     # if문의 코드블록은 뛰어쓰기 된곳까지
# elif a == b:
#     print("a b가 같다")
# else:  # if문의 조건이 거짓이면 코드 실행
#     print("if의 조건이 거짓일때 실행")

# print("종료")


# 예제 1
# # 🚨 여기는 그대로 👇
# number = int(input("숫자를 입력: \n"))
# # 🚨 여기는 그대로 👆

# # 아래에 코드 작성 👇
# if (number % 2 == 0):
#     print("짝수 입니다.")
# else:
#     print("홀수 입니다.")


# # 예제 2
# # 🚨 여기는 그대로 👇
height = int(input("키를 cm로 입력해 주세요: \n"))
# # 🚨 여기는 그대로 👆

# 아래에 코드 작성 👇
if height > 120:
    print("청룡열차를 탈수 있습니다.")
    age = int(input("나이를 입력해 주세요: \n"))
    # 입력받은 나이에 따라서 요금을 출력한다. if elif else 문 사용
    if age < 12:  # 12살 미만
        print("요금은 5000원 입니다.")
    elif age <= 18:  # 12살 이상 18살 이하
        print("요금은 7000원 입니다.")
    else:  # 19살 이상
        print("요금은 12000원 입니다.")
else:
    print("죄송하지만 탈수 없습니다.")