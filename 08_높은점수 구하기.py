# 🚨 여기는 그대로 👇
student_scores = input("학생들의 성적을 입력 :\n").split()
# split() => 기본공백(스페이스)로 입력된 값을 리스트로 저장
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  #성적 입력을 문자열로 받기 때문에 다시 정수로 변환해서 리스트에 입력
print(student_scores)
# 🚨 여기는 그대로 👆

# 아래에 코드 작성 👇
# highest_score = 0
# lowest_score = 999
# for n in student_scores:
#     if(n > highest_score):
#         highest_score = n
#     if(n < lowest_score):
#         lowest_score = n
# print(f"가장 높은 점수는 : {highest_score}")
# print(f"가장 낮은 점수는 : {lowest_score}")

print(f"가장 높은 점수는 : {max(student_scores)}")
print(f"가장 낮은 점수는 : {min(student_scores)}")