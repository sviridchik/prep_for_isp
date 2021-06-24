def ank(n,k):
    res = []
    passed = set()
    def rec(i):
        if len(res) < k:
            while i in passed:
                i += 1
            res.append(i)
            passed.add(i)
            while i < n:
                yield from rec(0)
                passed.remove(i)
                i += 1
                while i in passed:
                    i += 1

                res[-1] = i
                passed.add(i)
            i = res.pop()
            passed.remove(i)
        else:
            yield res


    return rec(0)
c = 0
for e in ank(4, 3):
    print(e)
    c+=1
print(c)
