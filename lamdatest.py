import inspect
from inspect import isfunction,ismethod
def myfun(x, fn):
    return fn(x)


result = myfun(5, lambda y: y ** 2)
print(result)


def myfun1(fn, *args, **kwargs):
    return fn(*args, **kwargs)


value = myfun1(lambda x, y: x ** y, 5, 3)
print("the value = ", value)
value1 = myfun1(lambda x, y: x + y, 5, y=25)
print(value1)

def myfun3(x,y,z=20,*,kw,kw2=12):
    return x+y
print(myfun3.__name__)
print(myfun3.__defaults__)
print(myfun3.__kwdefaults__)
print(myfun3.__code__.co_varnames)
print(myfun3.__code__.co_argcount)
print("From fun3")
print(inspect.getsource(myfun3))
print("From fun")
print(inspect.getsource(myfun))
print(inspect.isfunction(myfun3))
print(inspect.ismethod(myfun3))
print(inspect.isfunction(myfun))
print(inspect.ismethod(myfun))
print(inspect.getcomments(myfun3))
print(inspect.getmodule(isfunction))
print(inspect.getsource(myfun3))
print(callable(print))
list = [1,2,3,4]
result = list.append(5)
print(result)