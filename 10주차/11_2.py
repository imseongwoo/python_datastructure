parent = []
set_size = 0
sum = 0

def init_set(nSets):
    global set_size,parent
    set_size = nSets
    for i in range(nSets):
        parent.append(-1)

def find(id):
    while (parent[id] >= 0):
        id = parent[id]
    return id

def union(s1,s2):
    global set_size
    parent[s1]=s2
    set_size = set_size -1

def MSTKruskal(vertex,adj):
    vsize = len(vertex)
    init_set(vsize)
    eList = []
    global sum

    for i in range(vsize-1):
        for j in range(i+1,vsize):
            if adj[i][j] != None:
                eList.append((i,j,adj[i][j]))

    eList.sort(key=lambda e:e[2],reverse=True)

    edgeAccepted = 0
    while(edgeAccepted < vsize-1):
        e = eList.pop(-1)
        uset = find(e[0])
        vset = find(e[1])

        if uset != vset:        # 두 정점이 다른 집합의 원소이면 즉 ,사이클이 안생기면
            print("간선 추가 : (%s,%s,%d)"%(vertex[e[0]],vertex[e[1]],e[2]))
            union(uset,vset)    # 두 집합을 합함
            edgeAccepted += 1   # 간선 추가
            sum = sum + e[2]    # 가중치 값 더해주기


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

print('mst by kruskal')
MSTKruskal(vertex,weight)
print('가중치합 : ',sum)