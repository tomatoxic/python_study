# 숫자 맞추기 게임
import random
logo = '''
   ______                        _   __                __             
  / ____/_  _____  __________   / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                      
'''
print(logo)  #로고 출력
print("당신의 이름은 ?")
name = input()

print(f"안녕하세요 {name}님 1에서 20까지 숫자중 하나를 생각합니다.")
secretNumber = random.randint(1,20)  # 랜덤으로 숫자 하나 생성
print('6번안에 맞춰보세요')

for count in range(1, 7): # 6번의 맞출기회 
  guess = int(input("맞춰보세요 \n"))
  if (guess < secretNumber):
    print('그 숫자보다 큰수')
  elif (guess > secretNumber):
    print('그 숫자보다 작은수')
  else:
    break # 반복문 종료

if guess == secretNumber:
  print(f'잘 맞췄어요 {name}님 {count} 번만에 맞췄어요 !')
else:
  print(f'틀렸습니다. 정답은 {secretNumber} 입니다.')