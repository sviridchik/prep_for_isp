class StepTupenException(Exception):
    pass

class my_range():

    def __init__(self,start=0,end = None,step = 1):
        if step > 0:
            self.cur = start
            self.start = start
            self.end = end
            self.step = step
        else:
            raise StepTupenException



    def __iter__(self):
        return self

    def __next__(self):
        tmp = self.cur
        # yield (tmp)
        if self.cur<self.end:
            self.cur += self.step
        else:
            raise StopIteration
        return tmp

r = my_range(-1,end=6,step=2)
for i in r:
    print(i)