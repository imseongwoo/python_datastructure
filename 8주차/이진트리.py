# 원형큐 구현

MAX_QSIZE = 10
class CircularQueue:
    def __init__(self):
        self.front = 0
        self. rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1)%MAX_QSIZE
    def clear(self): self.front = self.rear

    def enqueue(self,item):
        if not self.isFull():
            self.rear = (self.rear+1) % MAX_QSIZE   # rear 회전
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)% MAX_QSIZE]

    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE


class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right



def preorder(n):
    if n is not None:
        print(n.data,end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data,end=' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data,end=' ')

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data,end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1+count_node(n.left)+count_node(n.right)


# 단말 노드 개수 구하기
def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)

# 트리의 높이

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if(hLeft > hRight):
        return hLeft+1
    else:
        return hRight + 1

# 높이 구하는 다른 함수
def getHeight(root):
    if root is None:
        return 0

    leftHeight = getHeight(root.left) + 1
    rightHeight = getHeight(root.right) + 1

    return max(leftHeight, rightHeight)


def test1():
    d = TNode('D',None,None)
    b = TNode('B',d,None)
    f = TNode('F',None,None)
    g = TNode('G',None,None)
    h = TNode('H',None,None)
    e = TNode('E',g,h)
    c = TNode('C',e,f)
    root = TNode('A',b,c)

    print('\n in-order:',end='')
    inorder(root)
    print()
    print('\n pre-order:',end='')
    preorder(root)
    print()
    print('\n post-order:',end='')
    postorder(root)
    print()
    print('\n level-order:',end='')
    levelorder(root)
    print()
    print('트리 노드 개수:',count_node(root))
    print('단말 노드 개수',count_leaf(root))
    print('트리 높이:',getHeight(root))

def test2():
    a = TNode('A',None,None)
    b = TNode('B',None,None)
    pab = TNode('/',a,b)
    c = TNode('C',None,None)
    pabc = TNode('*',pab,c)
    d = TNode('D',None,None)
    ppabc = TNode('*',pabc,d)
    e = TNode('E',None,None)
    root = TNode('+',ppabc,e)

    print('\n in-order:', end='')
    inorder(root)
    print()
    print('\n pre-order:', end='')
    preorder(root)
    print()
    print('\n post-order:', end='')
    postorder(root)
    print()
    print('\n level-order:', end='')
    levelorder(root)
    print()
    print('트리 노드 개수:', count_node(root))
    print('단말 노드 개수', count_leaf(root))
    print('트리 높이:', getHeight(root))

test1()
test2()