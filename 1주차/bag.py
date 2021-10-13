def contains(bag,e):
    return e in bag             #bag이라는 리스트에 e 라는 항목이 존재하면 true를 반환함

def insert(bag,e):
    bag.append(e)               # bag이라는 리스트에 e라는 항목을 추가함

def remove(bag,e):
    bag.remove(e)               # bag이라는 리스트에서 e라는 항목을 제거함

def count(bag):
    return len(bag)             # bag이라는 리스트의 길이를 반환함

def numOf(bag,e):
    return bag.count(e)

myBag = []

insert(myBag,'c++')
insert(myBag,'c++')

insert(myBag,'python')
insert(myBag,'java')
insert(myBag,'php')
insert(myBag,'django')

print(numOf(myBag,'c++'))
print(numOf(myBag,'python'))
print(numOf(myBag,'c+'))


# print('가방 속 물건:',myBag)
# print(contains(myBag,'c++'))
# print('가방 속 전체 항목 수:',count(myBag))
# remove(myBag,'c++')
#
# print('')
# print('가방 속 물건:',myBag)
# print(contains(myBag,'c++'))
#
# print('가방 속 전체 항목 수:',count(myBag))


