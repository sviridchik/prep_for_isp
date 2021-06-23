# # class LostPrecisionException(Exception):
# # 	pass
# a = 3//6
# # # print(a)
# assert a < 0
# # # if a == 0:
# # # 	raise Exception("oiu")
#
# # multiplier = lambda n: lambda k: n*k
#
# print(2>>1)

# a = (1,2,3)
# b = (4,5,6)
# c = a+b
# print(c)
# print(a<b)
# print(b<c)
# print(a<c)


def cubes(data):
    for el in data:
        yield (el**3)

def fib(n):
    f1, f2 = 1, 1
    res = []

    if n == 1:
        res.append(f1)
    if n == 2 or n>2:
        res.append(f1)
        res.append(f2)

    for i in range(n-2):
        res.append(f1+f2)
        f1_prev = f1
        f1 = f2
        f2 = f1_prev+f2
    return res

def fib_gen(n):
    f1, f2 = 1, 1
    f0 = 0
    # res = []
    #
    # if n == 1:
    #     yield (f1)
    # if n == 2:
    #     yield (f1)
    #     yield (f2)
    yield (1)
    for i in range(n):
        yield (f1 + f0)
        f0_prev = f0
        f0 = f1
        f1 = f0_prev + f1

# def fib(n):
#     f1=1
#     f2=1
#     for i in range(n):



# l = [1,2,3]
# c = cubes(l)
# # print(next(c))
# # print(next(c))
# for cc in c:
#     print(cc)

f = fib_gen(5)
for e in f:
    print(e)