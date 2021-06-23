import time
def dec(d_arg):
    log = {}
    def my_dec(fn):

        def wrapper(*args,**kwargs):
            if len(log.keys()) > d_arg:
                etalon = min([el[1] for el in log.values()])
                for k, v in log.items():
                    if v[1] == etalon:
                        del log[k]
                        break


            print(log)
            if (args,tuple(kwargs.items())) in log:
                print("again")

            else:
                res=[fn(*args,**kwargs),time.time()]
                log[(args,tuple(kwargs.items()))] = res
            return log[(args,tuple(kwargs.items()))][0]
        return wrapper
    return my_dec
@dec(2)
def ss(a,b):
    return a+b*2

print(ss(2,3))
print(ss(2,3))
print(ss(2,4))
print(ss(3,3))
print(ss(3,7))
print(ss(2,3))
print(ss(2,3))
#print(ss(2,3))


