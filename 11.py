

class Siglton_meta(type):
    data = {}
    # def __new__(mcs, name, parent, attr):
    #     return super().__new__(mcs,name, parent, attr)
    #
    #
    # def __init__(cls,name, parent, attr):
    #     super().__init__(cls.__name__, parent, attr)

    def __call__(cls, *args, **kwargs):
        name = cls.__name__
        # print(args)
        # print(kwargs)

        if cls.__name__ in Siglton_meta.data:
            att = (Siglton_meta.data[name].age,Siglton_meta.data[name].name)
            # print(att)
            print("я знаю ты тут есть", Siglton_meta.data[name])
            if att == args:
                print("absolutely")

            Siglton_meta.data[name].__init__(*args, **kwargs)
            return Siglton_meta.data[name]
        else:
            Siglton_meta.data[name]=super().__call__(*args,**kwargs)
            return Siglton_meta.data[name]

class Person(metaclass=Siglton_meta):
    def __init__(self,age,name):
        self.name = name
        self.age = age

inst1 = Person(12,"TOM")
print(inst1.age)
inst1.age *= 2
print(inst1.age)
inst2 = Person(12,"TOM")
print(inst2.age)
inst2.age *= 2
print(inst2.age)
inst3 = Person(22,"TOM")
print(inst3.age)