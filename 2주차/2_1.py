
income = int(input("연봉을 입력하세요 ==> "))
total = income
tax = 0

if income>15000:                    # 소득이 1억5천 초과일때
    tax += (income-15000)*0.38      # 소득에서 기준값을 뺀 후 근로소득세율을 곱한 값을 tax변수에 더해줌
    income = 15000                  # 소득 값을 기준값으로 바꿔준다

if income > 8800:                   # 동일처리
    tax += (income-8800)*0.35
    income = 8800

if income > 4600:                   # 동일처리
    tax += (income - 4600) * 0.24
    income = 4600

if income > 1200:                   # 동일처리
    tax += (income - 1200) * 0.15
    income = 1200

tax += income*0.06                  # 마지막 구간 처리
print("전체세금 = ", tax)            # 결과 값 출력
print("순수소득 = ", total - tax)
