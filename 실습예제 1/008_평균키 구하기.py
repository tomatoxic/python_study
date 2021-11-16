# 🚨 여기는 그대로 👇
student_heights = input("학생들의 키를 입력하세요\n").split()
# split() => 기본공백(스페이스)로 입력된 값을 리스트로 저장
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)
# 🚨 여기는 그대로 👆

# 아래에 코드 작성 👇

total_height = 0
for height in student_heights:
  total_height += height
print(f"전체 키의 합 = {total_height}")
print(f"학생 수 = {len(student_heights)}")
print(f"평균 키 = {total_height/len(student_heights)}")