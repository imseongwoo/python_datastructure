
class Bag:              # 클래스 함수 내에서 정의된 함수를 객체에서 호출하는 경우 제 1인자로 바로
            # 그 자신이 자동입력됨 따라서 인스턴스에서 호출할 함수 정의시 반드시 자동입력될 객체를 받아줄 변수를 self 등의 이름을 사용하여 표시해주어야함
    bag = []        # 클래스 안에서 리스트 생성

    def contains(self, e):
        return e in self.bag    # 클래스 안 리스트에 e 값이 있는지 확인한 후 있으면 true 없으면 false 반환

    def insert(self,e):
        self.bag.append(e)      # 클래스 안 리스트에 e 값 추가

    def remove(self,e):
        self.bag.remove(e)      # 클래스 안 리스트에서 e값 제거

    def count(self):
        return len(self.bag)    # 클래스 안 리스트의 길이 반환

    def numOf(self, e):
        return self.bag.count(e)    # 클래스 안 리스트에서 e의 개수 반환

myBag = Bag()
myBag.insert('휴대폰')
myBag.insert('지갑')
myBag.insert('손수건')
myBag.insert('빗')
myBag.insert('자료구조')
myBag.insert('야구공')
print('내 가방속의 물건:',myBag.bag)

myBag.insert('빗')
myBag.remove('손수건')
print('내 가방속의 물건:',myBag.bag)
print('리스트 길이 :',myBag.count())
print('가방안 해당 물건 개수 :',myBag.numOf('휴대폰'))