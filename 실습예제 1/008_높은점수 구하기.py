# ๐จ ์ฌ๊ธฐ๋ ๊ทธ๋๋ก ๐
student_scores = input("ํ์๋ค์ ์ฑ์ ์ ์๋ ฅ :\n").split()
# split() => ๊ธฐ๋ณธ๊ณต๋ฐฑ(์คํ์ด์ค)๋ก ์๋ ฅ๋ ๊ฐ์ ๋ฆฌ์คํธ๋ก ์ ์ฅ
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  #์ฑ์  ์๋ ฅ์ ๋ฌธ์์ด๋ก ๋ฐ๊ธฐ ๋๋ฌธ์ ๋ค์ ์ ์๋ก ๋ณํํด์ ๋ฆฌ์คํธ์ ์๋ ฅ
print(student_scores)
# ๐จ ์ฌ๊ธฐ๋ ๊ทธ๋๋ก ๐

# ์๋์ ์ฝ๋ ์์ฑ ๐
# highest_score = 0
# lowest_score = 999
# for n in student_scores:
#     if(n > highest_score):
#         highest_score = n
#     if(n < lowest_score):
#         lowest_score = n
# print(f"๊ฐ์ฅ ๋์ ์ ์๋ : {highest_score}")
# print(f"๊ฐ์ฅ ๋ฎ์ ์ ์๋ : {lowest_score}")

print(f"๊ฐ์ฅ ๋์ ์ ์๋ : {max(student_scores)}")
print(f"๊ฐ์ฅ ๋ฎ์ ์ ์๋ : {min(student_scores)}")