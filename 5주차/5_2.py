# 큐를 사용한 미로탈출 구현
from CircularQueue import *

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
def BFS():  # 너비우선  탐색
    que = CircularQueue() #원형큐 사용
    que.enqueue((0,1))  # 시작점 큐에 삽임
    print('bfs: ')

    while not que.isEmpty():    # dfs와 동일. 단, 원형큐의 메소드 사용
        here = que.dequeue()
        print(here,end='->')
        print()
        x,y = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x,y-1): que.enqueue((x,y-1)) # 상하좌우 검사
            if isValidPos(x, y + 1): que.enqueue((x, y + 1))
            if isValidPos(x-1, y ): que.enqueue((x-1, y ))
            if isValidPos(x+1, y ): que.enqueue((x+1, y ))

    return False

result = BFS()
if result:
    print('--> 미로탐색 성공')
else:
    print('--> 미로탐색 실패')