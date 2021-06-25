def lazy_flat_list(nested_list):
    for elem in nested_list:
        if isinstance(elem, list):
            yield from lazy_flat_list(elem)
        else:
            yield elem


nestedList = [[1, [1, [7, [9, 9], 8], 3]], 2, [1, 4, [6]]]

flat_list = []
for e in lazy_flat_list(nestedList):
    flat_list.append(e)
    # print(e)
print(flat_list)
