

class Ten():
    def __init__(self,iter_data):
        self.iter_data=iter_data
    def __iter__(self):
         (el for el in self.iter_data)
    def my_filter(self,lam):
        # res = []
        # for el in self.iter_data:
        #     if lam(el) is True:
        #         res.append(el)
        res = list(filter(lam,self.iter_data))
        self.iter_data=res[:]
