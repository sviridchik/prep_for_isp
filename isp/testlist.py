# #
# def merge(a,b):
#     i,j = 0,0
#     res = []
#     while i<len(a) and j<len(b):
#         if a[i]<=b[j]:
#             res.append(a[i])
#             i+=1
#         else:
#             res.append(b[j])
#             j+=1
#     res += a[i:] + b[j:]
#     return res
#
# def mergeSort(a):
#     if len(a) <=1:
#         return a
#     else:
#         l = a[:len(a)//2]
#         r = a[len(a)//2:]
#     return merge(mergeSort(l),mergeSort(r))
# #
# data = [1,9,-4,3,12,89]
# print(mergeSort(data))
#
# # def merge1(a,b):
# #     i,j,res = 0,0,[]
# #     while i<len(a) and j<len(b):
# #         if a[i]<=b[j]:
# #             res.append(a[i])
# #             i+=1
# #         else:
# #             res.append(b[j])
# #             j+=1
# #     res+=a[i:]+b[j:]
# #     return res
# #
# # def mergeSort1(a):
# #     if len(a)<=1:
# #         return a
# #     else:
# #         l = a[:len(a)//2]
# #         r = a[len(a)//2:]
# #     return merge1(mergeSort1(l),mergeSort1(r))
# #
# # print(mergeSort1(data))
import random
# def Quicksort(arr):
#     if len(arr)<=1:
#         return arr
#     pivot = random.choice(arr)
#     l = [el for el in arr if el < pivot]
#     m = [el for el in arr if el == pivot]
#     r = [el for el in arr if el >pivot]
#     return Quicksort(l)+m+Quicksort(r)
# data = [-2,9,3,1,-98,43]
#
# # print(Quicksort(data))
# def QuickSort(a):
#     if len(a)<=1:
#         return a
#     pivot = random.choice(a)
#     # l, r, m = [], [], []
#     l = [el for el in a if el<pivot]
#     r = [el for el in a if el>pivot]
#     m = [el for el in a if el == pivot]
#     # for el in a:
#     #     if el>pivot:
#     #         r.append(el)
#     #     elif el < pivot:
#     #         l.append(el)
#     #     else:
#     #         m.append(el)
#     return QuickSort(l)+m+QuickSort(r)
#
# data = [1,9,-4,3,12,89]
# print(QuickSort(data)

# a = [0,9,-2,8]
# b = [3,4,2]
# print(list(map(lambda x,y:x+y,a,b)))
# from collections import deque
#
# data = [[1,0,0,1,0,1],
#         [0,1,1,0,0,0],
#         [1,1,0,0,0,0],
#         [0,0,0,1,1,0],
#         [0,0,0,1,0,0],
#         [1,0,0,0,1,1]]
# n,m = 6,6
# count = 0
# data_info = set()
#
# for i in range(n):
#     for j in range(m):
#         if data[i][j] == 1 and (i,j) not in data_info:
#             orders = deque()
#             orders.append((i,j))
#             data_info.add((i,j))
#             while len(orders)>0:
#                 l = orders.popleft()
#                 if l[0]+1<n and data[l[0]+1][l[1]] == 1 and (l[0]+1,l[1]) not in data_info:
#                     orders.append((l[0]+1,l[1]))
#                     data_info.add((l[0]+1,l[1]))
#                 if 0 <= l[0] - 1 < n and data[l[0] - 1][l[1]] == 1 and (l[0] - 1, l[1]) not in data_info:
#                     orders.append((l[0] - 1, l[1]))
#                     data_info.add((l[0] - 1, l[1]))
#                 if 0 <= l[1] - 1 < m and data[l[0]][l[1] - 1] == 1 and (l[0], l[1] - 1) not in data_info:
#                     orders.append((l[0], l[1] - 1))
#                     data_info.add((l[0], l[1] - 1))
#                 if 0 <= l[1] + 1 < m and data[l[0]][l[1] + 1] == 1 and (l[0], l[1] + 1) not in data_info:
#                     orders.append((l[0], l[1] + 1))
#                     data_info.add((l[0], l[1] + 1))
#             count+=1
# print(count)


# class Siglton_meta(type):
#     data = {}
#     def __call__(cls, *args, **kwargs):
#         name = cls.__name__
#
#         if cls.__name__ in Siglton_meta.data:
#             att = (Siglton_meta.data[name].age,Siglton_meta.data[name].name)
#             # print(att)
#             print("я знаю ты тут есть", Siglton_meta.data[name])
#             if att == args:
#                 print("absolutely")
#
#             Siglton_meta.data[name].__init__(*args, **kwargs)
#             return Siglton_meta.data[name]
#         else:
#             Siglton_meta.data[name]=super().__call__(*args,**kwargs)
#             return Siglton_meta.data[name]
#
# # class S(type):
# #     data = {}
# #
# #     def __call__(cls, *args, **kwargs):
# #         name = cls.__name__
# #         if name in S.data:
# #             print("я знаю ты тут есть", Siglton_meta.data[name])
# #             if S.data[name][0] == args and S.data[name][1] == kwargs:
# #                 print("absolutely")
# #                 return S.data[name][-1]
# #             else:
# #                 S.data[name][0] = args
# #                 S.data[name][1] = kwargs
# #                 S.data[name][-1].__init__(*args, **kwargs)
# #                 return S.data[name][-1]
# #         else:
# #             res = [args,kwargs]
# #             l = super().__call__(*args, **kwargs)
# #             res.append(l)
# #             S.data[name]=res
# #             return S.data[name][-1]
#
# class S(type):
#     data = {}
#
#     def __call__(cls, *args, **kwargs):
#         name = cls.__name__
#         print(args,kwargs)
#         if name in S.data:
#             print("я знаю ты тут есть", S.data[name])
#             attr = (S.data[name].age,S.data[name].name)
#             print(attr,"l")
#             if attr == args:
#                 print("absolutely")
#             return S.data[name]
#             # else:
#             #     S.data[name].__init__(*args, **kwargs)
#             #     return S.data[name]
#         else:
#             # res = [args,kwargs]
#             l = super().__call__(*args, **kwargs)
#             # resappend(l)
#             S.data[name]=l
#             return S.data[name]
#
# class Person(metaclass=S):
#     def __init__(self,age,name):
#         self.name = name
#         self.age = age
#
#
# inst1 = Person(12,"TOM")
# print(inst1.age)
# inst1.age *= 2
# print(inst1.age)
# inst2 = Person(12,"TOM")
# print(inst2.age)
# inst2.age *= 2
# print(inst2.age)
# inst3 = Person(22,"TOM")
# print(inst3.age)

# def merge(a,b):
#     res = []
#     i,j = 0,0
#     while i<len(a) and j<len(b):
#         if a[i]<b[j]:
#             res.append(a[i])
#             i+=1
#         else:
#             res.append(b[j])
#             j+=1
#     res+=a[i:]+b[j:]
#     return res
#
# def sort(a):
#     if len(a)<=1:
#         return a
#     l = a[:len(a)//2]
#     r = a[len(a)//2:]
#     return merge(sort(l),sort(r))
#
# data = [-2,9,3,1,-98,43]
# print(sort(data))

def Quicksort(a):
    if len(a)<=1:
        return a
    pivot = random.choice(a)
    l = [el  for el in a if el<pivot]
    m = [el for el in a if el==pivot]
    r = [el for el in a if el > pivot]
    return Quicksort(l)+m+Quicksort(r)

data = [-2,9,3,1,-98,43]
print(Quicksort(data))
