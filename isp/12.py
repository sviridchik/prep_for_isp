# def maker():
def dec(cls):
    log = {}
    class wr(cls):
        def __new__(cls, *args, **kwargs):
            name = cls.__name__
            if name in log:
                return log[name]
            else:
                log[name] = super().__new__(cls)
                return log[name]

    return wr
    # def wrapper(*args,**kwargs):
    #     name = cls.__name__
    #     if name in log:
    #         if log[name][0] != args or log[name][1] != kwargs:
    #             log[name][-1].__init__(*args,**kwargs)
    #     else:
    #         res = [args,kwargs]
    #         l = type.__call__(*args,**kwargs)
    #         res.append(l)
    #         log[name] = res
    #     return log[name]
    # return wrapper
    # # return dec

@dec
class Person():
    def __init__(self,age,name):
        self.name = name
        self.age = age

inst1 = Person(12,"TOM")
print(inst1.age)
inst1.age *= 2
print(inst1.age)
inst2 = Person(12,"TOM")
print(inst1 is inst2)
print(inst2.age)
inst2.age *= 2
print(inst2.age)
inst3 = Person(22,"TOM")
print(inst3.age)
print(inst2 is inst3)
