
#
def cnk(n,k):
    i = 0
    res = []

    def r1(i):
        if len(res)==k:
            yield res
            #return

        res.append(i)

        for j in range(i+1,n+1):
            rr = r1(j)
            for el in rr:
                yield el
            res[ - 1] = j
        res.pop()

    r =  r1(i)
    for el in r:
        yield el

# data = [1,2,3]
for e in cnk(6,3):
    print(e)

# def fn3():
#     print('fn3')
#
# def fn2():
#     print('start fn2')
#     fn3()
#     print('exit fn2')
#
# def fn1():
#     print('start fn1')
#     fn2()
#     print('exit fn1')

# fn1()


# def sochet(n, m):
#     res = []
#
#     def rec(i):
#         if len(res) == m:
#             yield res.copy()
#             return
#
#         while i < n:
#             res.append(i)
#             for res_t in rec(i + 1):
#                 yield res_t
#             # rec(i + 1)
#             i += 1
#             res.pop()
#
#     for res in rec(0):
#         yield res
#
#
# ans = list()
# for e in sochet(3, 2):
#     ans.append(e)
#     print(e)
# print(len(ans))