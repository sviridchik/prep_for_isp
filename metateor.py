class my_metaclass(type):
    def __new__(mcs, class_name, parents, attributes):
        print(f'- my_metaclass.__new__ - Creating class instance of type', mcs)
        return super().__new__(mcs, class_name, parents, attributes)

    def __init__(cls, class_name, parents, attributes):
        print('- my_metaclass.__init__ - Initializing the class instance', cls)
        super().__init__(class_name, parents, attributes)

    def __call__(cls, *args, **kwargs):
        print('- my_metaclass.__call__ - Creating object of type ', cls)
        return super().__call__(*args, **kwargs)

    # def fn(cls, x):
    #     print(f'In fn with x = {x}')


def my_class_decorator(cls):
    print('- my_class_decorator - Chance to modify the class', cls)
    return cls


@my_class_decorator
class MyClass(metaclass=my_metaclass):

    def __new__(cls):
        print('- C.__new__ - Creating object.')
        return super(MyClass, cls).__new__(cls)

    def __init__(self):
        print('- C.__init__ - Initializing object.')

    def __call__(self, *args, **kwargs):
        print(f'- Call of instance {self}')


print('- Before creating instance')
instance = MyClass()
print('Object instance =', instance)
instance()
# MyClass.fn(6)
