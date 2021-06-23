class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree():
    def __init__(self):
        self.root = None

    def search_iteratively(self,x):
        v = self.root
        while v is not None:
            if v.value == x:
                return v
            elif x < v.value:
                v = v.left
            else:  # x > v.value:
                v = v.right
        return None

    def insert_iteratively(self,x):
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
    res = 0
    def debth(self,node,h =1):

        if node is None:
            return
        print(node.value)
        # h += 1
        if node.left is not None:
            self.debth(node.left,h+1)


        if node.right is not None:
            self.debth(node.right,h+1)

        if not (node.right or node.left):
            if h>Tree.res:
                Tree.res = h



t  = Tree()
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
t.debth(t.root)
print(t.res)
print()
