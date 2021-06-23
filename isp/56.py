class Node:
    def __init__(self, value = 0, next =None):
        self.value=value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield (node)
            node=node.next

    def add(self,node):
        node= Node(node)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            current = self.tail
            # while current.next is not None:
            #     current = current.next
            # current.next = node
            current.next = node
            self.tail = node

    def __repr__(self):
        res = []
        for el in self:
            res.append(el.value)
        res = list(map(lambda x:str(x) ,res))
        return " -> ".join(res)
    #
    # def get_previous(self,node):
    #     current = self.head
    #     while current.next != node:
    #         current = current.next
    #     return current


    def delete_duplicates(self):
        data = []
        prev = self.head
        for el in self:
            if el.value in data:
                # prev = self.get_previous(el)
                prev.next = el.next
            else:
                data.append(el.value)
                prev = el
        return self.head

    def partition(self,x):
        l = []
        r = []
        for el in self:
            if el.value<=x:
                l.append(el)
                if len(l)>=2:
                    l[-2].next = l[-1]

            else:
                r.append(el)
                if len(r) >= 2:
                    r[-2].next = r[-1]
        self.head = l[0]
        # for i in range(len(l)-1):
        #     l[i].next = l[i+1]
        # for i in range(len(r)-1):
        #     r[i].next = r[i+1]
        if len(r)>=1:
            l[-1].next = r[0]
            r[-1].next = None
            self.tail = r[-1]

        return self

l = LinkedList()
# l.add(3)
# l.add(5)
# l.add(-9)
# l.add(5)
# l.add(5)
# l.add(33)
# l.add(5)
# print(l)
# l.delete_duplicates()
# print(l)
l.add(1)
l.add(4)
l.add(4)
l.add(3)
l.add(2)
l.add(5)
l.add(1)
l.add(2)
# l.add(5)
print(l)
l.delete_duplicates()
print(l)
l.partition(3)
print(l)