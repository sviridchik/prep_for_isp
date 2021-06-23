class Singleton():
    data = {}
    def __new__(cls, *args, **kwargs):
        name = cls.__name__
        if name not in Singleton.data:
            l = object.__new__(cls)
            res = [args, kwargs, l]
            Singleton.data[name] = res

        return Singleton.data[name][-1]


class Person(Singleton):
    # def __new__(cls, *args, **kwargs):
    #    return super(Person, cls).__new__(cls)
    def __init__(self, age, name):
        self.name = name
        self.age = age

inst1 = Person(12, "TOM")
print(inst1.age)
inst1.age *= 2
print(inst1.age)
inst2 = Person(12, "TOM")
print(inst1 is inst2)
print(inst2.age)
inst2.age *= 2
print(inst2.age)
inst3 = Person(22, "TOM")
print(inst3.age)
print(inst2 is inst3)