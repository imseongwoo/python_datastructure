class Node:
    def __init__(self,elem,next = None):
        self.data = elem
        self.link = next


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self): return self.head == None # 공백상태 검사
    def clear(self): self.head = None
    def size(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.link
            count += 1
        return count
    def getNode(self,pos):      # pos번째 노드 반환
        if pos<0 : return None
        node = self.head        # node는 head부터 시작
        while pos > 0 and node != None:     # pos번 반복
            node = node.link       # node를 다음 노드로 이동
            pos -= 1            # 남은 반복 횟수 줄임
        return node             # 최종 노드 반환

    def getEntry(self,pos):
        node = self.getNode(pos)
        if node == None: return None
        else: return node.data

    def insert(self,pos,elem):
        before = self.getNode(pos-1)        # 이전 노드를 찾음
        if before == None:                  # 맨 앞에 삽입하는 경우
            self.head = Node(elem,self.head)    # 맨 앞에 삽임
        else:
            node = Node(elem,before.link)   # 새 노드를 만들어 새 노드가 앞노드를 가리키게함
            before.link = node              # 이전노드가 새 노드를 가리키게함

    def delete(self,pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link


class Term:
    def __init__(self,expon,coeff):
        self.expon = expon
        self.coeff = coeff

class SparsePoly(LinkedList):
    def __init__(self):
        super().__init__()

    def degree(self):       # 차수
        if self.head == None: return 0
        else: return self.head.data.expon

    def display(self,msg=""):
        print("\t",msg,end='')

        node = self.head
        while node is not None: # 모든 노드 확인
            print("%5.1f x^%d + " %(node.data.coeff,node.data.expon),end='')
            node = node.link
        print()


    def read(self):
        self.clear()
        while True:
            token = input("계수 차수 입력(종료:-1): ").split(" ")
            if token[0] == '-1':        # -1 입력시 입력 다항식 표시 후 return
                self.display("입력 다항식:")
                return
            self.insert(self.size(), Term(int(token[1]), float(token[0])))  # 노드 삽입

    def add(self, bb):

        pA = self.head
        pB = bb.head
        pC = SparsePoly()
        sum = 0
        while pA is not None and pB is not None:        # 두 다항식에 노드가 있는 동안 반복
            if (pA.data.expon == pB.data.expon):    # 지수가 같은 경우
                sum = pA.data.coeff + pB.data.coeff     # 계수끼리 더해준다
                pC.insert(pC.size(),Term(int(pA.data.expon),sum))   # 새로운 클래스에 삽입해준다.
                pA = pA.link    # 다음 노드
                pB = pB.link    # 다음 노드
            elif pA.data.expon > pB.data.expon:     # A다항식의 지수가 더 큰 경우
                pC.insert(pC.size(),Term(int(pA.data.expon),float(pA.data.coeff)))  # 그대로 넣어줌
                pA =pA.link
            else:   # 작은경우
                pC.insert(pC.size(),Term(int(pB.data.expon),float(pB.data.coeff)))
                pB = pB.link

        if pB == None:      # 반복하고 남은 노드 처리
            pC.insert(pC.size(),Term(int(pA.data.expon),float(pA.data.coeff)))
        elif pA == None:
            pC.insert(pC.size(), Term(int(pB.data.expon), float(pB.data.coeff)))

        return pC

a = SparsePoly()
b = SparsePoly()
c = SparsePoly()
a.read()
b.read()
c = a.add(b)
a.display("A = ")
b.display("B = ")
c.display("A + B = ")
