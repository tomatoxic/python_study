# while 반복문
# while True:
#     print("무한반복")

# count = 0
# while count < 3:
#     print('횟수: ', count)
#     count += 1

# name = ''
# while name != '펭수':  # name이 펭수가 되면 종료
#     name = input('펭수를 입력해 주세요 : ')
# print("thank you")

# hit = 0
# while hit <10:
#         hit += 1
#         if hit % 2 == 0: # hit가 짝수이면
#                 continue # 반복문 계속
#         print(f'나무를 {hit}번 찍었습니다.')
#         if hit == 5:
#             break # 5회면 반복문 종료

# # []는 파이썬 리스트 타입, 반복문 for는 이 리스트안의 내용을 한 번씩 반복
# for n in [1,2,3]:
#         print(n)

# for s in ["다람쥐", "펭귄", "낙타", '아나콘다', '하이에나']:
#         print(s)

# # 문자열도 리스트로 처리해서 하나씩 출력
# for c in '홍길동님':
#         print(c) 

# # for 반복문과 자주쓰는 함수 range()
# for n in range(3): # 0부터 3-1까지
#         print(n)

# # 1에서 100까지 합은
# total = 0
# for x in range(1,101):
#         total += x
# print('1에서 100까지 합은',total,'입니다.')

# # 구구단 2단
# for i in range(1,10):
#         print(f'2 X {i} = {2*i}')

# 구구단 9단까지 가로로 출력
for x in range(2,10): # 2단부터 9단까지
        print()
        for i in range(1,10): # 1부터 9까지 곱하기
                print(f'[{x} X {i} = {x*i}]', end = ' ')
        

        