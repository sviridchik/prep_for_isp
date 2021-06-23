class Node:
    def  __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def add(self, node):
#         mode = Node(node)
#         if self.root is None:
#             self.root = node
#         else:


tree = [5,8,20,15,14,16,30,9,6,7]
tree = [Node(el) for el in tree]
tree[0].left = tree[1]
tree[0].right = tree[2]

tree[1].left = tree[3]
tree[1].right = tree[4]

tree[2].right = tree[5]

tree[4].left = tree[6]
tree[4].right = tree[7]

tree[7].left = tree[8]

tree[8].left = tree[9]


print()


def hren_ustala_zadolbalo(node):

    if node.left is not None:

        l = hren_ustala_zadolbalo(node.left)
        for el in l:
            yield el
        yield (node)

        if node.right is not None:
            r = hren_ustala_zadolbalo(node.right)
            for el in r:
                yield el
        else:
            return
    else:

        yield(node)

        if node.right is not None:
          r =  hren_ustala_zadolbalo(node.right)
          for el in r:
              yield el
        else:
            return



def hren_ustala_zadolbalo1(node):

    if node.left is not None:
        # yield from hren_ustala_zadolbalo1(node.left)
        l = hren_ustala_zadolbalo1(node.left)
        for el in l:
            yield el

    yield (node)

    if node.right is not None:
        r =  hren_ustala_zadolbalo1(node.right)
        for el in r:
          yield el
    # else:
    #     # yield (node)
    #     return

uu = hren_ustala_zadolbalo1(tree[0])
for u in uu:
    print(u.value)