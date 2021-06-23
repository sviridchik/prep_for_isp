import collections
class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree():
    def __init__(self):
        self.root = None

    def search_iteratively(self, x):
        v = self.root
        while v is not None:
            if v.value == x:
                return v
            elif x < v.value:
                v = v.left
            else:  # x > v.value:
                v = v.right
        return None

    def insert_iteratively(self, x):
        parent = None
        v = self.root
        while v is not None:
            parent = v
            if x < v.value:
                v = v.left
            elif x > v.value:
                v = v.right
            else:  # x == v.value
                return

        w = Node(x)

        if parent is None:
            self.root = w
        elif x < parent.value:
            parent.left = w
        elif x > parent.value:
            parent.right = w

    def debth(self, node):

        if node is None:
            return
        print(node.value)
        # h += 1
        l,r=0,0
        if node.left is not None:
            l = self.debth(node.left)


        if node.right is not None:
            r = self.debth(node.right)
        return max(l,r)+1
        #
        # if not (node.right or node.left):
        #     if h > Tree.res:
        #         Tree.res = h

    def bfs(self):
        ch = 1
        orders = collections.deque()
        orders.append((self.root,ch))
        #cur = self.root
        while len(orders)>0:
            l,ch = orders.popleft()
            print(l.value)

            # ch=orders[0][1]

            if l.left is not None:
                orders.append((l.left,ch+1))

            if l.right is not None:
                orders.append((l.right,ch+1))


            # if len(orders)>0:
            #     l = orders[0][0]
        print("h = ",ch)


t = Tree()
t.insert_iteratively(9)
t.insert_iteratively(3)
t.insert_iteratively(12)
t.insert_iteratively(-4)
t.insert_iteratively(4)
t.insert_iteratively(10)
t.insert_iteratively(24)
t.insert_iteratively(5)
t.insert_iteratively(28)
t.insert_iteratively(6)

h = t.debth(t.root)
print()
print(h)
print()
t.bfs()