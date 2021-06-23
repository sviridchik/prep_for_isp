
class ModelCreator(type):
    data = {"StringField": str, "IntegerField": int}
    data_info = {}
    def __new__(mcs,name, parent, attr):
        for k,v in attr.items():
            if type(v).__name__ in ModelCreator.data:
                ModelCreator.data_info[k] = ModelCreator.data[type(v).__name__]
        return super().__new__(mcs,name,parent,attr)

    def __call__(cls, *args, **kwargs):
        for k,v in kwargs.items():
            if type(v) != ModelCreator.data_info[k]:
                raise AttributeError
           # else:
           #     setattr(cls,k,v)
        name = cls.__name__
        #return super().__call__()
        inst = cls.__new__(cls)
        for k, v in kwargs.items():
            setattr(inst, k, v)
        return inst
        # return super().__new__(cls,name,*args, **kwargs)


class StringField:
    pass

class IntegerField:
    pass

class Student(metaclass=ModelCreator):
    name = StringField()
    age = IntegerField()
    bv = 7
    # def __init__(self, *args, **kwargs):
     #   print(kwargs)

   # def __new__(cls):
    #    return super().__new__(cls)



s = Student(name='toha')
s2 = Student(name='vikuha')
print(s.name)
print(s2.name)
print(s.age)