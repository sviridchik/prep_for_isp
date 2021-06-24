
def cnk(n,k):
    res = []
    def rec(i):
        if len(res)<k:
            res.append(i)
            for j in range(n-i):
                l = rec(i+1)
                for el in l:
                    yield el
                i += 1
                res[-1]=i
            res.pop()
        else:
            yield res

            return


    return rec(0)

r = cnk(5,3)
for rr in r:
    print(rr)