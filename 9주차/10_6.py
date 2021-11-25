def find_connected_component(graph,vertax):
    visited = [0]*(len(vertax)+1)       # 방문 확인 리스트
    colorList = []              # 부분그래프별 정점 리스트

    for i in range(len(vertax)):        # 그래프의 모든 정점들
        if not visited[i]:              # 방문하지 않았다면 조건문 실행
            color = dfs_cc(graph,[],vertax,i,visited)   # 정점을 의미하는 i를 넘겨줌
            colorList.append(color)     # 연결성분리스트 추가


    return len(colorList)   # 개수반환

def dfs_cc(graph,color,vertax,i,visited):
    if not visited[i]:
        visited[i] = 1      # 방문처리
        color.append(vertax[i]) # 리스트에 방문노드 추가
        for a in range(len(vertax)):
            if graph[i][a] and not visited[a]:  # 인접하는 노드들 중 방문하지 않은 노드면
                dfs_cc(graph,color,vertax,a,visited)    # 순환호출
    return color        # 리스트 반환




def find_bridges(adj,vtx):
    n = len(vtx)
    count = 0
    for i in range(n):      # 모든 간선에 대해서
        for j in range(i+1,n):
            if adj[i][j] != 0:      # 간선이 존재하면
                adj[i][j] = adj[j][i] = 0   # 간선을 없애 준 후 연결성분검사 함수 실행
                if find_connected_component(adj,vtx)>1:     # 값이 1보다 크다면 연결이 끊어진것이므로
                    count += 1              # count 증가
                    print("Bridge%d: (%s,%s)"%(count,vtx[i],vtx[j]))        # 브릿지된 노드 출력
                adj[i][j] = adj[i][j] = 1   # 간선 원상복구




vertex = ['A','B','C','D','E','F','G','H']
vertex2 = ['A','B','C','D','E','F']
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

adjMat2 = [
    [0,1,0,1,0,0],
    [1,0,1,1,1,0],
    [1,1,0,0,0,1],
    [0,1,0,0,1,0],
    [0,1,0,1,0,0],
    [0,0,1,0,0,0]
]
find_bridges(adjMat2,vertex2)