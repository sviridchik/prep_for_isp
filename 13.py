"""
1)quick
2)merge
3)radix
"""
import random

def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = random.choice(arr)
    l,m = [],[]
    r = []
    for el in arr:
        if el<pivot:
            l.append(el)
        elif el>pivot:
            r.append(el)
        else:
            m.append(el)
    return quicksort(l)+m+quicksort(r)


def Quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = random.choice(arr)
    l = [el for el in arr if el < pivot]
    m = [el for el in arr if el == pivot]
    r = [el for el in arr if el >pivot]
    return Quicksort(l)+m+Quicksort(r)
data = [-2,9,3,1,-98,43]

print(Quicksort(data))

#2merge
def merge(a,b):
    i,j,res = 0,0,[]
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    res+=a[i:]+b[j:]
    return res

def mergeSort(a):
    if len(a)<=1:
        return a
    else:
        l = a[:len(a)//2]
        r = a[len(a)//2:]
    return merge(mergeSort(l),mergeSort(r))

# print(mergeSort(data))


# 3 radix
def radix(a):
    rang = 10
    length = len(str(max(a)))
    for i in range(length):
        b = [[] for k in range(rang)]
        for x in a:
            figure = x//10**i%10
            b[figure].append(x)
        a = []
        for k in range(rang):
            a = a + b[k]
    print(a)

# radix(data)