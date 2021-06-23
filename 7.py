
name = "1.json"

class Person():
    pass

def decor(cl):
    with open(name,"r") as f:
        data1 = f.read()
        data = eval(data1)


    # cl.__init__(self,data.json)
    class Res(cl):
        def __init__(self,*args,**kwargs):
            super(Res, self).__init__(*args,**kwargs)
            for k,v in data.items():
                setattr(self,k,v)
                # self.k = v
            # cl.__init__(self)
            
    return Res

print(decor(Person)().name)