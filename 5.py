import types
class Logger:
    def __init__(self):
        self.log = []

    def __str__(self):
         s =""
         for el in self.log:
             print(el[0])

    def decor(self,f):
        def wrapper(*args, **kwargs):
            res = []
            res.append(f.__name__)
            res.append(args)
            res.append(kwargs)
            self.log.append(res)
            s = f(*args, **kwargs)
            res.append(s)
            return s
        return wrapper


    def __getattribute__(self, item):
        # print(item)
        if isinstance(super().__getattribute__(item),types.MethodType) and item!= "decor":
            print("я функция")
            # res = []
            # res.append(item)
            l = self.decor(super().__getattribute__(item))
        else:
            l = super().__getattribute__(item)
        # return super().__getattribute__(item)
        return l

class A(Logger):

    def met1(self,el):

        return "чего надо {}".format(el)

    x = 6

a = A()
# print(a.x)
print(a.met1(9))
print(a.met1(10))
print(a.log)
