# 우선순위 큐 구현
class PriorityQueue:
    def __init__(self):     # 생성자
        self.items = []     # 항목저장 리스트

    def isEmpty(self):      # 공백상태 검사
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items=[]

    def enqueue(self,item):     # 정렬된 배열을 이용하기 위해 알맞은 인덱스를 반복문을 통해 찾은후 삽임
        indexnum = 0
        for i in range(self.size()):
            if item[2] > self.items[i][2]:
                indexnum = i
        self.items.insert(indexnum,item)

    def dequeue(self):  # 우선순위 순으로 정렬되어 있으므로 pop()만 해주면 된다.

        return self.items.pop()

