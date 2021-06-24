# # # #
# # # def merge(a,b):
# # #     i,j = 0,0
# # #     res = []
# # #     while i<len(a) and j<len(b):
# # #         if a[i]<=b[j]:
# # #             res.append(a[i])
# # #             i+=1
# # #         else:
# # #             res.append(b[j])
# # #             j+=1
# # #     res += a[i:] + b[j:]
# # #     return res
# # #
# # # def mergeSort(a):
# # #     if len(a) <=1:
# # #         return a
# # #     else:
# # #         l = a[:len(a)//2]
# # #         r = a[len(a)//2:]
# # #     return merge(mergeSort(l),mergeSort(r))
# # # #
# # # data.json = [1,9,-4,3,12,89]
# # # print(mergeSort(data.json))
# # #
# # # # def merge1(a,b):
# # # #     i,j,res = 0,0,[]
# # # #     while i<len(a) and j<len(b):
# # # #         if a[i]<=b[j]:
# # # #             res.append(a[i])
# # # #             i+=1
# # # #         else:
# # # #             res.append(b[j])
# # # #             j+=1
# # # #     res+=a[i:]+b[j:]
# # # #     return res
# # # #
# # # # def mergeSort1(a):
# # # #     if len(a)<=1:
# # # #         return a
# # # #     else:
# # # #         l = a[:len(a)//2]
# # # #         r = a[len(a)//2:]
# # # #     return merge1(mergeSort1(l),mergeSort1(r))
# # # #
# # # # print(mergeSort1(data.json))
# # import random
# # # def Quicksort(arr):
# # #     if len(arr)<=1:
# # #         return arr
# # #     pivot = random.choice(arr)
# # #     l = [el for el in arr if el < pivot]
# # #     m = [el for el in arr if el == pivot]
# # #     r = [el for el in arr if el >pivot]
# # #     return Quicksort(l)+m+Quicksort(r)
# # # data.json = [-2,9,3,1,-98,43]
# # #
# # # # print(Quicksort(data.json))
# # # def QuickSort(a):
# # #     if len(a)<=1:
# # #         return a
# # #     pivot = random.choice(a)
# # #     # l, r, m = [], [], []
# # #     l = [el for el in a if el<pivot]
# # #     r = [el for el in a if el>pivot]
# # #     m = [el for el in a if el == pivot]
# # #     # for el in a:
# # #     #     if el>pivot:
# # #     #         r.append(el)
# # #     #     elif el < pivot:
# # #     #         l.append(el)
# # #     #     else:
# # #     #         m.append(el)
# # #     return QuickSort(l)+m+QuickSort(r)
# # #
# # # data.json = [1,9,-4,3,12,89]
# # # print(QuickSort(data.json)
# #
# # # a = [0,9,-2,8]
# # # b = [3,4,2]
# # # print(list(map(lambda x,y:x+y,a,b)))
# # # from collections import deque
# # #
# # # data.json = [[1,0,0,1,0,1],
# # #         [0,1,1,0,0,0],
# # #         [1,1,0,0,0,0],
# # #         [0,0,0,1,1,0],
# # #         [0,0,0,1,0,0],
# # #         [1,0,0,0,1,1]]
# # # n,m = 6,6
# # # count = 0
# # # data_info = set()
# # #
# # # for i in range(n):
# # #     for j in range(m):
# # #         if data.json[i][j] == 1 and (i,j) not in data_info:
# # #             orders = deque()
# # #             orders.append((i,j))
# # #             data_info.add((i,j))
# # #             while len(orders)>0:
# # #                 l = orders.popleft()
# # #                 if l[0]+1<n and data.json[l[0]+1][l[1]] == 1 and (l[0]+1,l[1]) not in data_info:
# # #                     orders.append((l[0]+1,l[1]))
# # #                     data_info.add((l[0]+1,l[1]))
# # #                 if 0 <= l[0] - 1 < n and data.json[l[0] - 1][l[1]] == 1 and (l[0] - 1, l[1]) not in data_info:
# # #                     orders.append((l[0] - 1, l[1]))
# # #                     data_info.add((l[0] - 1, l[1]))
# # #                 if 0 <= l[1] - 1 < m and data.json[l[0]][l[1] - 1] == 1 and (l[0], l[1] - 1) not in data_info:
# # #                     orders.append((l[0], l[1] - 1))
# # #                     data_info.add((l[0], l[1] - 1))
# # #                 if 0 <= l[1] + 1 < m and data.json[l[0]][l[1] + 1] == 1 and (l[0], l[1] + 1) not in data_info:
# # #                     orders.append((l[0], l[1] + 1))
# # #                     data_info.add((l[0], l[1] + 1))
# # #             count+=1
# # # print(count)
# #
# #
# # # class Siglton_meta(type):
# # #     data.json = {}
# # #     def __call__(cls, *args, **kwargs):
# # #         name = cls.__name__
# # #
# # #         if cls.__name__ in Siglton_meta.data.json:
# # #             att = (Siglton_meta.data.json[name].age,Siglton_meta.data.json[name].name)
# # #             # print(att)
# # #             print("я знаю ты тут есть", Siglton_meta.data.json[name])
# # #             if att == args:
# # #                 print("absolutely")
# # #
# # #             Siglton_meta.data.json[name].__init__(*args, **kwargs)
# # #             return Siglton_meta.data.json[name]
# # #         else:
# # #             Siglton_meta.data.json[name]=super().__call__(*args,**kwargs)
# # #             return Siglton_meta.data.json[name]
# # #
# # # # class S(type):
# # # #     data.json = {}
# # # #
# # # #     def __call__(cls, *args, **kwargs):
# # # #         name = cls.__name__
# # # #         if name in S.data.json:
# # # #             print("я знаю ты тут есть", Siglton_meta.data.json[name])
# # # #             if S.data.json[name][0] == args and S.data.json[name][1] == kwargs:
# # # #                 print("absolutely")
# # # #                 return S.data.json[name][-1]
# # # #             else:
# # # #                 S.data.json[name][0] = args
# # # #                 S.data.json[name][1] = kwargs
# # # #                 S.data.json[name][-1].__init__(*args, **kwargs)
# # # #                 return S.data.json[name][-1]
# # # #         else:
# # # #             res = [args,kwargs]
# # # #             l = super().__call__(*args, **kwargs)
# # # #             res.append(l)
# # # #             S.data.json[name]=res
# # # #             return S.data.json[name][-1]
# # #
# # # class S(type):
# # #     data.json = {}
# # #
# # #     def __call__(cls, *args, **kwargs):
# # #         name = cls.__name__
# # #         print(args,kwargs)
# # #         if name in S.data.json:
# # #             print("я знаю ты тут есть", S.data.json[name])
# # #             attr = (S.data.json[name].age,S.data.json[name].name)
# # #             print(attr,"l")
# # #             if attr == args:
# # #                 print("absolutely")
# # #             return S.data.json[name]
# # #             # else:
# # #             #     S.data.json[name].__init__(*args, **kwargs)
# # #             #     return S.data.json[name]
# # #         else:
# # #             # res = [args,kwargs]
# # #             l = super().__call__(*args, **kwargs)
# # #             # resappend(l)
# # #             S.data.json[name]=l
# # #             return S.data.json[name]
# # #
# # # class Person(metaclass=S):
# # #     def __init__(self,age,name):
# # #         self.name = name
# # #         self.age = age
# # #
# # #
# # # inst1 = Person(12,"TOM")
# # # print(inst1.age)
# # # inst1.age *= 2
# # # print(inst1.age)
# # # inst2 = Person(12,"TOM")
# # # print(inst2.age)
# # # inst2.age *= 2
# # # print(inst2.age)
# # # inst3 = Person(22,"TOM")
# # # print(inst3.age)
# #
# # # def merge(a,b):
# # #     res = []
# # #     i,j = 0,0
# # #     while i<len(a) and j<len(b):
# # #         if a[i]<b[j]:
# # #             res.append(a[i])
# # #             i+=1
# # #         else:
# # #             res.append(b[j])
# # #             j+=1
# # #     res+=a[i:]+b[j:]
# # #     return res
# # #
# # # def sort(a):
# # #     if len(a)<=1:
# # #         return a
# # #     l = a[:len(a)//2]
# # #     r = a[len(a)//2:]
# # #     return merge(sort(l),sort(r))
# # #
# # # data.json = [-2,9,3,1,-98,43]
# # # print(sort(data.json))
# #
# # # def Quicksort(a):
# # #     if len(a)<=1:
# # #         return a
# # #     pivot = random.choice(a)
# # #     l = [el  for el in a if el<pivot]
# # #     m = [el for el in a if el==pivot]
# # #     r = [el for el in a if el > pivot]
# # #     return Quicksort(l)+m+Quicksort(r)
# # #
# # # data = [-2,9,3,1,-98,43]
# # # print(Quicksort(data))
# # import inspect,re
# # #
# # # class MetaClass(type):
# # #
# # #     def __init__(cls,name, parents, attr):
# # #         with open("data.json", "r") as f:
# # #             data = eval(f.read())
# # #         for k,v in data.items():
# # #             setattr(cls,k,v)
# # #
# # #         super(MetaClass,cls).__init__(name, parents, attr)
# # #
# # # class A(metaclass=MetaClass):
# # #     pass
# #
# #
# # # a = A()
# # # print(inspect.getmembers(A))
# # # print(a.age)
# # # #
# # # class cm(type):
# # #
# # #     def __init__(cls,*args,**kwargs):
# # #         with open("data.json") as f:
# # #             data = eval(f.read())
# # #         for k,v in data.items():
# # #             # print(k,v)
# # #             setattr(cls,k,v)
# # #         super(cm, cls).__init__(cls)
# # #
# # #
# # # class P(metaclass=cm):
# # #     pass
# # #
# # # p = P()
# # # print(p.name)
# # # pat = r"[+-/*\d\[\](){}]*"
# #
# # # ex = "(1+3)*[14/2]()[{{}}]"
# #
# # #
# # # ex = "(1+3)*[14/2]"
# # # pat = r"[+-/*\d\[\](){}]*"
# # # r = re.fullmatch(pat,ex)
# # # print(r)
# # # if r is not None:
# # #     print("ok")
# # #     flag =True
# # #     pat_open = "[({"
# # #     pat_close = "])}"
# # #     stack = []
# # #     for el in ex:
# # #         if el in pat_open:
# # #             stack.append(el)
# # #         elif el in pat_close:
# # #             if len(stack) == 0:
# # #                 flag = False
# # #                 break
# # #             else:
# # #                 if pat_close.index(el) == pat_open.index(stack[-1]):
# # #                     stack.pop()
# # #                 else:
# # #                     flag = False
# # #                     break
# # #     if len(stack)!=0:
# # #         flag = False
# # #     if flag:
# # #         print("okokok")
# # #     else:
# # #         print("unbalanced")
# # import time,types
# #
# # def dec_maker(d_arg,size):
# #     data = {}
# #     if isinstance(d_arg,types.FunctionType):
# #         print("ok")
# #     else:
# #         raise AttributeError
# #     def dec(f):
# #         def wrapper(args):
# #             print(args)
# #             args.sort(key = d_arg)
# #             print(args)
# #             tmp = (f.__name__,tuple(args))
# #
# #             if tmp in data:
# #                 return data[tmp][0]
# #             else:
# #                 if len(data.keys())>size:
# #                     etalon = min([el[0] for el in data.values()])
# #                     for k,v in data:
# #                         if v[0]==etalon:
# #                             del data[k]
# #
# #                 data[tmp] = [f(args), time.time()]
# #                 return data[tmp][0]
# #         return wrapper
# #     return dec
# #
# # @dec_maker(lambda x:x[0],2)
# # def f(a):
# #     print(a)
# #
# # a = [(0,3),(-3,4)]
# # # b = [(3,-4),(0,-3)]
# # f(a)
# class Node:
#     def  __init__(self, value=0, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
# # class Tree:
# #     def __init__(self):
# #         self.root = None
# #
# #     def add(self, node):
# #         mode = Node(node)
# #         if self.root is None:
# #             self.root = node
# #         else:
#
#
# tree = [5,8,20,15,14,16,30,9,6,7]
# tree = [Node(el) for el in tree]
# tree[0].left = tree[1]
# tree[0].right = tree[2]
#
# tree[1].left = tree[3]
# tree[1].right = tree[4]
#
# tree[2].right = tree[5]
#
# tree[4].left = tree[6]
# tree[4].right = tree[7]
#
# tree[7].left = tree[8]
#
# tree[8].left = tree[9]
#
#
# print()
#
#
#
# def straight(node):
#
#
#     if node.left is not None:
#         yield from straight(node.left)
#     yield node
#     if node.right is not None:
#         yield from straight(node.right)
#
# r = straight(tree[0])
# for rr in r:
#     print(rr.value)

class Node:
    def __init__(self, value = 0, next =None):
        self.value=value
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,node):
        node = Node(node)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            cur = self.tail
            cur.next = node
            self.tail  = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        res = []
        for el in self:
            res.append(el.value)
        res = list(map(lambda x: str(x), res))
        return " -> ".join(res)


