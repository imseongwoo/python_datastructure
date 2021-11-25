INF = 9999
sum = 0
def getMinVertex(dist,selected):
    global sum
    minv = 0
    mindist = INF
    for v in range(len(dist)):  # 모든 정점들에 대해
        if not selected[v] and dist[v] < mindist:   # 선택이 안되어있고 가중치가 작으면
            mindist = dist[v]       # 갱신
            minv = v    # 최소 가중치의 정점 갱신
    sum = sum + mindist
    return minv

def MSTPrim(vertex,adj):
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize
    dist[0] = 0

    for i in range(vsize):
        u = getMinVertex(dist,selected)
        selected[u] = True
        print(vertex[u],end=' ')

        for v in range(vsize):
            if (adj[u][v] != None):
                if selected[v] == False and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]
    print()

vertex = ['A','B','C','D','E','F','G','H','I']
weight = [
    [None,4,None,None,None,None,None,7,None],
    [4,None,8,None,None,None,None,11,None],
    [None,8,None,7,None,4,None,None,2],
    [None,None,7,None,9,14,None,None,None],
    [None,None,None,9,None,10,None,None,None],
    [None,None,4,14,10,None,2,None,None],
    [None,None,None,None,None,2,None,1,6],
    [7,11,None,None,None,None,1,None,7],
    [None,None,2,None,None,None,6,7,None]
]
MSTPrim(vertex,weight)
print(' 가중치 합 : ',sum)