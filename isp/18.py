import types
def dec_arg(d_arg):
    print(type(d_arg))
    if isinstance(d_arg,types.FunctionType):
        print("ok")
    else:
        raise AttributeError

    def my_dec(f):
        def wrapper(args):
            print(args)
            print("magic begin")
            args.sort(key = d_arg)
            print(args)
            return f(args)
        return wrapper
    return my_dec

@dec_arg(lambda x:x[-1] )
def fn(l):
    print("i am ffff")
    for el in l:
        print("f",el)


l = [(9,8),(-4,-9),(5,6),(7,-3)]
fn(l)
