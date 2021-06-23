class Node:
    def __init__(self, value = 0, next =None):
        self.value=value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield (node)
            node=node.next

    def add(self,node):
        node= Node(node)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def __repr__(self):
        res = []
        for el in self:
            res.append(el.value)
        res = list(map(lambda x:str(x) ,res))
        return " -> ".join(res)

    def get_previous(self,node):
        current = self.head
        while current.next != node:
            current = current.next
        return current


    def delete_duplicates(self) :
        data = []
        for el in self:
            if el.value in data:
                prev = self.get_previous(el)
                prev.next = el.next
            else:
                data.append(el.value)
        return self.head

    def partition(head: Node, x: int):
        pass