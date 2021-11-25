class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right



def level(root,node):
    q = []
    q.append(root)
    level = 1
    q.append(None)      # q에 1레벨 탐색을 마치기 위해 넣어줌. 반복문 안에서 조건문으로 각 레벨 탐색이 끝났을 경우 처리
    while len(q):       # q값이 존재하면 계속 반복
        temp = q[0]     # 맨 앞 노드를 temp에 넣어줌
        q.pop(0)        # 맨 앞 노드 처리
        if(temp == None):   # None 값을 통해서 한 레벨의 탐색이 끝났을 때 처리 가능
            if len(q) == 0:     # q가 비어있으면, 찾는 노드가 트리안에 들어있지 않는 것을 의미하므로 0 반환
                return 0
            if (q[0] != None):  # q가 비어있지 않으면 다음 레벨 처리를 위해 None 삽입
                q.append(None)
            level += 1  # 한 레벨 탐색이 끝났으므로 레벨 +1

        else:
            if(temp.data == node.data):     # 찾는 값과 일치한다면 레벨값 반환
                return level
            if temp.left:       # 노드의 왼쪽자식 노드나 오른쪽 자식노드가 존재한다면 처리를 위해 q에 삽입해줌
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

    return 0


d = TNode('D',None,None)
e = TNode('E',None,None)
b = TNode('B',d,e)
f = TNode('F',None,None)
c = TNode('C',None,f)
root = TNode('A',b,c)

g = TNode('GG',None,None)       # 트리안에 없는 노드
lev = level(root,g)

print('g노드가 있는 레벨:',lev)
print('f노드가 있는 레벨:',level(root,f))
print('b노드가 있는 레벨:',level(root,b))
print('a노드가 있는 레벨:',level(root,root))