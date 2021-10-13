import random

answer = random.randint(1,99)       # 결과값 임의 설정

min = 0     # 범위의 최소값
max = 99    # 범위의 최대값

for a in range(10):             # 10번 동안 반복 a=0~9까지
    guess = int(input("숫자를 입력하세요(범위 : %d~%d)" %(min,max)))  # 예측값을 입력받아 변수에 넣어줌, min부터 max까지의 범위 출력
    if guess == answer:     # 예측값과 답이 일치한다면
        print("정답입니다! %d번만에 맞추셨습니다" %(a+1)) # a+1 값이 총 반복한 횟수
        break       # break문을 통해 반복문을 빠져나감 -> "이후 게임이 끝났습니다" 문장 출력
    elif guess > answer:    # 예측값이 정답보다 크다면
        print("더 작은 숫자입니다.")
        max = guess     # 범위의 최대값을 예측값으로 바꿔줌

    else:       # 예측값이 정답보다 작다면
        print("더 큰 숫자입니다.")
        min = guess     # 범위의 최소값을 예측값으로 바꿔줌


print("게임이 끝났습니다.")
