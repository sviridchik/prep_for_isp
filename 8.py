

def decorator(fn):
    log =[]
    def wrapper(*args,**kwargs):
        for i in range(len(log)):
            if fn.__name__ in log[i]:
                if log[i][1] == args and log[i][2] == kwargs:
                    print(log[i],"cash")
                    # res = fn(*args, **kwargs)
                    return log[i][-1]

        res=fn(*args,**kwargs)
        l = []
        l.append(fn.__name__)
        l.append(args)
        l.append(kwargs)
        l.append(res)
        log.append(l)
        return res
    return wrapper

@decorator
def a (a,b):
    return a+b

print(a(1,2))
print(a(1,2))