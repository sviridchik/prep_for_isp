# l = [1,2,3,4]
# print(l.reverse())
# print(reversed(l))
# class Person:
#     pass
# name = "1.json"
# def decor(cl):
#     with open(name,"r") as f:
#         data.json = eval(f.read())
#
#     class Res (cl):
#         def __init__(self,*args,**kwargs):
#             super(Res, self).__init__(*args,**kwargs)
#             for k,v in data.json.items():
#                 setattr(Res,k,v)
#
#
#     return Res
#
# print(decor(Person)().age)
import types
class Logger():
    def __init__(self):
        self.log = []
    def decor(self,fn):
        def wrapper(*args,**kwargs):
            res = []
            res.append(fn.__name__)
            res.append(args)
            res.append(kwargs)
            s = fn(*args,**kwargs)
            res.append(s)
            self.log.append(res)
            return s
        return wrapper

    def __getattribute__(self, item):
        res = super(Logger, self).__getattribute__(item)
        if isinstance(res,types.MethodType) and item!="decor":
            l = self.decor(res)
        else:
            l = super(Logger, self).__getattribute__(item)
        return l

    def __str__(self):
        s = ""
        for e in self.log:
            print(e)
        return s

class A(Logger):
    def kk(self,a,v):
        return ("hgfgfg  {}:{}".format(a,v))
    def vv(self,c,d):
        return c+d

aa = A()
print(aa.kk(2,3))
print(aa.vv(8,2))
print(aa)
