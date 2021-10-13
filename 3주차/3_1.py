class Polynomial :
    def __init__(self):
        self.coef = []

    def degree(self):
        return len(self.coef)-1

    def display(self, msg="f(x) =  "):
        print(" ",msg,end='')
        deg = self.degree()

        for n in range(deg,0,-1):
            if self.coef[n] == 0:       # 계수가 0일 경우에는 출력을 하지 않고 continue를 사용해 다음 반복문으로 넘어감
                continue
            elif self.coef[n] < 0:      # 계수가 음수일 경우에는 부호를 따로 출력하지 않음
                print("%5.1f x^%d  "%(self.coef[n],n),end='')
            else:                       # 계수가 양수일 때 +를 붙여 출력
                print(" +%5.1f x^%d " % (self.coef[n], n), end='')

        if self.coef[0] > 0:            # 상수 값이 양수일때 +를 붙여 출력
            print("+%4.1f"%self.coef[0])
        elif self.coef[0] <0:           # 상수값이 음수일때 그대로 출력
            print("%4.1f" % self.coef[0])
        else:                           # 상수값이 0이면 출력하지 않는다
            print()
    def multi(self,b):
        pm = Polynomial()
        pm.coef = [0] * (len(self.coef) + len(b.coef) - 1)      # 다항식 곱셈의 길이만큼 0으로 초기화함 ex) 2차 방정식끼리 곱하면 3+3-1 =5 [0]*5
        for i in range(len(self.coef)):                         # 이중 반복문을 통해 모든 계수끼리 곱해준다
            for j in range(len(b.coef)):                        # i나 j가 0일 때는 상수를 의미한다.
                pm.coef[i + j] += self.coef[i] * b.coef[j]      # 곱해준 값을 pm의 리스트에 차수에 알맞게 저장함

        return pm


    def add(self,b):
        p = Polynomial()
        if self.degree() > b.degree():
            p.coef = list(self.coef)            # 두 값의 차수 중 큰 차수의 coef리스트를 새로운 객체 p에 복사
            for i in range(b.degree()+1):       # 차수가 작은 다항식의 길이만큼 반복하여 덧셈 처리
                p.coef[i] += b.coef[i]
        else:
            p.coef = list(b.coef)
            for i in range(self.degree()+1):
                p.coef[i] += self.coef[i]
        return p

    def subtraction(self,b):        # 뺄셈기능
        new = self.neg(b)           # b의 부호를 반대로 만들어주는 함수 실행

        return self.add(new)        # 부호를 반대로 만들어준값을 더해줌

    def neg(self,temp):             # 부호를 반대로 만들어주는 함수
        new = Polynomial()          # 새로운 객체 생성
        new.coef = list(temp.coef)  # b의 원래 차수로 초기화해줌
        for a in range(len(temp.coef)): # 모든 수에 대해서 반복
            new.coef[a] = -temp.coef[a] # 부호를 반대로 저장해줌
        return new


    def eval(self,x):
        sum = 0                     # 내부반복문이 끝난 후에 계산 값을 저장해놓을 변수
        temp = 1                    # 내부반복문 안에서 x의 n승을 계산하고 저장해놓을 변수
        for a in range(1,self.degree()+1):  # 1차식부터 최고차항까지 계산
            for b in range(a):      # 1차는 1번 반복 2차는 2번반복 3차는 3번 반복하게 a로 범위 제한
                temp = temp*x       # 인수 x로 받은 값 대입
            temp = temp * self.coef[a]  # 계수 곱하기
            sum += temp             # 마지막에 반환할 값에 더해주기
            temp = 1                # 다음 계산을 위해 변수를 다시 1로 초기화해줌
        return sum+self.coef[0]     # 미지수가 없는 0차까지 더해준 후 반환

def read_poly():
    instr = input("최고차항부터 차수를 순서대로 입력하세요:").split()     # 스페이스바로 나누어 입력받은 변수를 저장함
    p = Polynomial()            # 객체를 생성하면 생성자 함수가 호출되어 리스트 생성
    for coef in instr:
        val = float(coef)       # 계수를 실수로 저장함
        p.coef.insert(0,val)    # 새로운 리스트 맨 앞에 변수 저장
    return p                    # 객체 반환

if __name__ == "__main__":
    a = read_poly()
    b = read_poly()
    c = a.add(b)
    d = a.subtraction(b)
    e = a.multi(b)
    a.display("A(x) =")
    b.display("B(x) =")
    c.display("C(x) =")
    d.display("D(x) =")
    e.display("e(x) =")

    print("c(2) =",c.eval(2))






