# from decimal import Decimal
#
# print(callable(Decimal))
# result = Decimal(20.3)
# print(type(result))
# print(callable(result))
#
#
# class myClass:
#     def __init__(self, x=1):
#         self.counter = 0
#         print("this is init")
#         self.counter += x
#
#
# myObj = myClass()
# print(myClass.__init__(myObj, 20))
#
# print(callable(myObj.__init__))
# print(myObj.counter)
#
# print("After callable")
# print(myObj.counter)
#
# List = [1, 'a', 3, 'b', 4]
# iterator = iter(List)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
#
# def fact(n):
#     return 1 if n < 1 else n * fact(n - 1)
#
#
# result = list(map(fact, range(6)))
# print(result)
# for i in result:
#     print(i)
# for x in result:
#     print(x)
#
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [10, 11, 12, 13, 14, 15, 16]
# results = list(map(lambda x, y: x + y, list1, list2))
# for ii in results:
#     print(ii)
#
# val = zip(list1, list2)
# print(val)
# for jj in val:
#     print(jj)
#
#
# def myGen():
#     data = 1
#     while data < 10:
#         square = data * data
#         yield square
#         data += 1
#
#
# value = myGen()
# print(value)
# for j in value:
#     print(j)
#
# name1 = ["jin", "suga", "rm", "jhope", "jimin", "v", "jk"]
#
#
# def name(name1):
#     name2 = ["jin", "jimin", "jk"]
#     if (name1 in name2):
#         return 1
#     else:
#         return 0
#
#
# number = filter(name, name1)
# print(number)
# for n in number:
#     print(n)
#
# import functools
#
# print(functools.reduce(lambda a, b: a + b, list1))
# print(functools.reduce(lambda c, d: c * d, list2))
# print(functools.reduce(lambda e, f: e if e < f else f, list2))
# print(functools.reduce(lambda a, b: a if a > b else b, list1))
#
#
# def mysum(x, y):
#     return x + y
#
#
# def reduce(mysum, seq):
#     first = seq[0]
#     for m in seq[1:]:
#         first = mysum(first, m)
#     return first
#
#
# value1 = reduce(mysum, list2)
# print(value1)
#
# from functools import partial
#
#
# def myfun(x, y, z):
#     x = x + 10
#     y = y + 10
#     z = z + 10
#     print(x, y, z)
#
#
# output = partial(myfun, 20)
# output(30, 40)


# def myfun1(a, b, *args, a1, b1, **kwargs):
#     print(a, b, *args, a1, b1, **kwargs)
#
#
# newFun = partial(myfun1, 10, a1="testing")
# newFun(30,40,b1='exam',c=20,d=30,e=40)


import operator
from functools import reduce

# list = [10,20,30,40,50]
# list1=[11,5,23,61,85]
# output1 = reduce(lambda x,y:x*y,list)
# print(output1)
# output2 = reduce(operator.truediv,list)
# print("output from output2",output2)
# a = operator.gt(list,list1)
# print(a)
# print(dir(operator))


# def outerFun():
#     g = 'green'
#     def innerFun():
#         nonlocal g
#         g='purple'
#         print(g)
#     innerFun()
#     print(g)
# outerFun()


# def outter():
#     data = "this is data"
#
#     def inner():
#         print(data)
#
#     return inner
#
#
# obj = outter()
# del outter
# obj()
#
#
# def adding(n):
#     def adding1(data):
#         return data + n
#
#     return adding1
#
#
# add10 = adding(10)
# add20 = adding(20)
# print(add20(20))
# print(add10(10))
# print(add20(add10(5)))
# print(add20.__closure__[0].cell_contents)
# print(add10.__closure__[0].cell_contents)
#
# import operator
#
#
# def myFun(x, y):
#     print(x / y)
#
#
# def get(fn):
#     def inner(x, y):
#         if operator.lt(x, y):
#             x, y = y, x
#         return fn(x,y)
#
#     return inner
#
#
# a = int(input("enter your first number"))
# b = int(input("enter your second number"))
# result = get(myFun)
# result(a, b)


"""The counter function"""
import operator


def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("function call{0} for the {1} time".format(fn.__name__, count))
        return fn(*args, **kwargs)

    return inner



def add(x, y=0):
    """The add function"""
    print(x + y)


def sub(x, y):
    """The sub function"""
    if operator.lt(x, y):
        x, y = y, x
    print(x - y)



a = int(input("enter your first number"))
b = int(input("enter your second number"))

result = counter(add)
result(a, b)

result1 = counter(sub)
result1(a, b)


def mydec1(fn):
    def inner():
        print("this is my dec1")
        return fn()

    return inner


def mydec2(fn):
    def inner():
        print("this is my dec2")
        return fn()

    return inner


@mydec1
@mydec2
def myfun():
    print("this is myfun")


myfun()


from functools import wraps
def docing(fn):
    @wraps(fn)
    def inner(*args,**kwargs):
        print("This is from inner function")
        return fn(*args,**kwargs)
    return inner

@docing
def fun1(x,y):
    """This is function1"""

    print("This is from function1")
    return x+x+y

@docing
def fun2(x,y):
    """This is function2"""
    print("This is from function2")
    return x+y+y

c = int(input("enter data1"))

d = int(input("enter data2"))

result = docing(fun1(c,d))
print(fun1.__doc__)
print(fun1.__name__)
result1= docing(fun2(c,d))
print(fun2.__doc__)
print(fun2.__name__)

