
from queue import Queue


def dfs(v):
    stack = [v]     # 스택을 만들고 시작 노드를 넣어줌

    visited = [0] * (len(vertex)+1)     # 방문 여부 체크 리스트
    visited[v] = 1              # v 노드 방분

    while stack:
        temp = stack.pop()      # 스택의 윗부분부터 방문
        print(vertex[temp],end=' ')

        for i in range(len(vertex)):
            if adjMat[temp][i] and not visited[i]:      # 방문한적이 없고 인접행렬 값이 1이면
                stack.append(i)             # 스택에 추가
                visited[i] = 1              # 해당 노드 방문 처리




def bfs(v):
    queue = Queue()      # 큐 구현을 위해 Queue라이브러리 사용
    queue.put(v)
    visited = [False] * (len(vertex)+1) # 방문 정보 리스트
    visited[v] = True   # 현재 노드 방문 처리

    while queue:    # 큐가 빌 때까지 반복
        temp = queue.get()  # 큐에서 앞 원소를 뽑아 출력
        print(vertex[temp],end=' ')

        for i in range(len(vertex)):
            if adjMat[temp][i] and not visited[i]:      # 방문한적이 없고 인접행렬 값이 1이면
                queue.put(i)             # 큐에 추가
                visited[i] = True              # 해당 노드 방문 처리

vertex = ['A','B','C','D','E','F','G','H']
adjMat = [
    [0,1,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,1,0,0,0],
    [0,1,1,0,0,1,0,0],
    [0,0,1,0,0,0,1,1],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,1],
    [0,0,0,0,1,0,1,0]
]
print('dfs : ',end='')
dfs(0)
print()
print('bfs : ',end='')
bfs(0)