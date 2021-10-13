# 우선순위 큐를 이용한 미로탈출
import math
from PriorityQueue import *
(ox,oy) = (9,8)

map = [['1','1','1','1','1','1','1','1','1','1'],
       ['e','0','0','0','0','0','0','0','0','1'],
       ['1','1','1','0','0','1','1','1','1','1'],
       ['1','1','1','1','0','1','1','1','1','1'],
       ['1','1','1','1','0','1','1','1','1','1'],
       ['1','1','1','1','0','1','1','1','1','1'],
       ['1','1','1','1','0','1','1','1','1','1'],
       ['1','1','1','1','0','0','0','0','0','1'],
       ['1','1','1','1','1','1','1','1','0','x'],
       ['1','1','1','1','1','1','1','1','1','1']]
MAZE_SIZE = 10

def isValidPos(x,y):
    if x<0 or y<0 or x>= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def dist(x,y):
    (dx,dy) = (ox-x,oy-y)
    return math.sqrt(dx*dx+dy*dy)

def MySmartSearch():
    q = PriorityQueue()
    q.enqueue((0,1,1/dist(0,1)))
    print('PQueue: ')

    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2],end='->')
        x,y,_ = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x,y-1): q.enqueue((x,y-1,-dist(x,y-1))) # 상하좌우 검사
            if isValidPos(x, y + 1): q.enqueue((x, y + 1,-dist(x,y+1)))
            if isValidPos(x-1, y ): q.enqueue((x-1, y,-dist(x-1,y) ))
            if isValidPos(x+1, y ): q.enqueue((x+1, y,-dist(x+1,y) ))
        print('우선순위큐: ',q.items)
    return False

result = MySmartSearch()
if result:
    print('--> 미로탐색 성공')
else:
    print('--> 미로탐색 실패')