def creator(parametr):
    print(f"see parametr {parametr}")
    def my_dec(f):
        print(f"see parametr {parametr}")
        def wrapper(*args,**kwargs):
            print(f"see par and args... {parametr} {args} {kwargs}")
            f(*args,**kwargs)
        return wrapper
    return my_dec

@creator(parametr=1)
def f (*args, **kwargs):
    print("hi")

f(8, 9, k=9)