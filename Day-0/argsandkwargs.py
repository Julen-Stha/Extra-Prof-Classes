##args
def sum(*args):
    print(type(args))
    print(args)
    a=0
    for i in args:
        a += i
    return a

#kwargs
def address(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key,value in kwargs.items():
        print(f"{key}: {value}")


sum_all = sum(1,2,3,4,5,90)
print(sum_all)
address(name="alice", address="KTM")

