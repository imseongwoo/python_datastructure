class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right


def is_complete_binary_tree(root):
    if root is None:    # 빈 트리는 완전이진트리
        return True

    queue = []  # 빈 리스트 선언

    flag = False    # flag변수 선언

    queue.append(root)  # 루트노드를 삽입한 후에 반복문 시작
    while queue:
        tn = queue.pop(0)     # 맨 앞 노드를 꺼냄

        # 왼쪽 자식노드나 오른쪽 자식노드가 존재하고 flag변수가 참이면 완전이진트리가 아님
        if (tn.left):
            if flag == True:
                return False

            queue.append(tn.left)

        else:        # 왼쪽 자식이 존재하지 않으면 flag 값을 참으로 설정함
            flag = True


        if (tn.right):
            if flag == True:        # 마지막 레벨의 왼쪽 자식노드가 존재하지 않으면 flag값이 True이므로 완전이진트리가 아님
                return False

            queue.append(tn.right)

        else:       # 오른쪽 자식이 존재하지 않으면 flag 값을 참으로 설정함
            flag = True

    return True     # 반복문이 끝나면 완전이진트리임

d = TNode('D',None,None)
e = TNode('E',None,None)
b = TNode('B',d,e)
f = TNode('F',None,None)
c = TNode('C',None,f)
root = TNode('A',b,c)

print(is_complete_binary_tree(root))
if is_complete_binary_tree(root) == True:
    print('완전이진트리')
else:
    print('완전이진트리 아님')

"""
            A
          /   \
         B     C
        / \     \
       D   E     F

"""