def lazy_perest(n):
    res = []
    passed = set()

    def rec(i):
        if len(res) == n:
            yield res
            return

        while i in passed:
            i += 1
        res.append(i)
        passed.add(i)
        while i < n:
            yield from rec(0)
            el = res.pop()
            passed.remove(el)
            i += 1
            while i in passed:
                i += 1

            res.append(i)
            passed.add(i)

        el = res.pop()
        passed.remove(el)

    yield from rec(0)


ans = []
for e in lazy_perest(4):
    ans.append(e)
    print(e)

print(len(ans))