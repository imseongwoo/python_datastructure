class Set:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def delete(self,elem):
        if elem in self.items:
            self.items.remove(elem)

    def insert(self,elem):
        if elem in self.items: return
        for idx in range(len(self.items)):
            if elem < self.items[idx] :
                self.items.insert(idx,elem)
                return
        self.items.append(elem)

    def intersect(self,setB):
        c = Set()
        a=0
        b=0
        while a < len(self.items) and b < len(setB.items):  # 두 집합 중 하나라도 조건에 부합하지 않으면 종료됨 (정렬되었기 때문에 한 집합을 전부 체크하면 더이상 겹치는 값은 존재하지 않음)
            vala = self.items[a]
            valb = setB.items[b]

            if vala < valb:         # 정렬되어 있기 때문에 작은값의 리스트 인덱스를 1씩 증가시킨다
                a += 1
            elif vala > valb:
                b += 1
            else:                   # 값이 같으면 해당 값을 집합에 넣어주고 인덱스를 동시에 1씩 증가시킨다.
                c.items.append(vala)
                a += 1
                b += 1

        return c

    def difference(self,setB):      # 차집함 구하기

        c = Set()                   # 값 변경 방지를 위해 새로운 Set 객체에 값 복사
        c = self

        val = self.intersect(setB)  # 차집합을 구하기 위해 두 집합의 교집합을 구한다

        for a in val.items:     # 교집합의 값을 반복문을 통해서 c에서 제거해준다.
            c.items.remove(a)

        return c            # 계산 완료된 집합 반환




a = Set()
b = Set()

a.insert(0)
a.insert(2)
a.insert(1)
a.insert(5)
# a.insert(3)
# a.insert(11)
# a.insert(14)

b.insert(1)
b.insert(2)
b.insert(3)
b.insert(14)
print('첫번째 집합 : ',a.items)
print('두번째 집합 : ',b.items)

c = a.intersect(b)
d = a.difference(b)

print('교집합 : ',c.items)
print('차집합 : ',d.items)