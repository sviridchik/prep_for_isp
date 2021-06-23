import math

class DimdifensionException(Exception):
    pass
    # def __init__(self,e):
    #     print(e)

class Vector:
    e = "Error dim"
    def __init__(self, coords):
        self.coords = coords

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise DimdifensionException("Error dim")
        coord_news=list([sum(p) for p in zip(self.coords, other.coords)])
        return Vector(coord_news)

    def __mul__(self, other):
        if isinstance(other,int):
           coord_new = [el*other for el in self.coords]
           return Vector(coord_new)

    def length(self)->float:
        l = math.sqrt(sum(list(map(lambda x:x**2,self.coords))))
        return l
    def __str__(self):
        return "".join(map(lambda x:str(x) ,self.coords))
    def __eq__(self, other):
        if len(self.coords) != len(other.coords):
            return False
        else:
           return all([pair[0] == pair[1] for pair in zip(self.coords,other.coords)])

    def __getitem__(self, key):
        if isinstance(key,int):
            if 0<=key<len(self.coords):
                return self.coords[key]
            else:
                raise IndexError("index error")
        else:
            raise TypeError("type error")

vect1 = Vector([5, 3, -1])
vect2 = Vector([0, 10, -6])
vect3 = Vector([5, 3, -1])


print(vect1==vect3)
print((vect1.length()))
print(vect1+vect2)
print(vect3)
#
print(f'is {vect1} equal {vect2}: {vect1 == vect2}')
print(f'is {vect1} not equal {vect2}: {vect1 != vect2}')
print(f'is {vect1} equal {vect3}: {vect1 == vect3}')
print(f'is {vect1} not equal {vect3}: {vect1 != vect3}')

print(f'{vect1} + {vect2} = {vect1 + vect2}')
print(f'{vect1} + {vect3} = {vect1 + vect3}')

# print(f'{vect1} - {vect2} = {vect1 - vect2}')
# print(f'{vect1} - {vect3} = {vect1 - vect3}')

print(f'{vect1} * {vect2}: {vect1 * vect2}')
print(f'{vect1} * {vect3}: {vect1 * vect3}')

# print(f'len({vect1}) = {len(vect1)}')
# print(f'len({vect2}) = {len(vect2)}')

print(f'{vect1}[2] = {vect1[2]}')
print(f'{vect2}[1] = {vect2[1]}')

print(f'{vect1}.length() = {vect1.length()}')
print(f'{vect2}.length() = {vect2.length()}')

print(f'{vect1} * 3: {vect1 * 3}')
print(f'{vect2} * 3: {vect2 * 3}')