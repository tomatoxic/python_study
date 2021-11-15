hit = 0
while hit <10:
        hit += 1
        if hit % 2 == 0: # hit가 짝수이면
                continue # 반복문 계속
        print(f'나무를 {hit}번 찍었습니다.')
        if hit == 5:
            break # 5회면 반복문 종료


