class unflat_iter:
    def __init__(self, iterable):
        self.iters_stack = [iterable.__iter__()]

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if len(self.iters_stack) == 0:
                raise StopIteration

            try:
                e = self.iters_stack[-1].__next__()
                break
            except StopIteration:
                self.iters_stack.pop()

        if isinstance(e, list):
            self.iters_stack.append(e.__iter__())

            return self.__next__()
        else:
            return e
        # for e in iterable:
        #     if isinstance(e, list):
        #         for el in unflat_iter(e):
        #             yield el
        #     else:
        #         yield e


nestedList = [[1, [1, 3]], 2, [1, 4, [6, [9], 8], -3]]
for e in unflat_iter(nestedList):
    print(e)
# gen = (e for e in range(5))
# for i in range(8):
#     print(gen.__next__())
