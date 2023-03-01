# def logger(fn):
#     from datetime import timezone,datetime
#     from functools import wraps
#     @wraps(fn)
#     def inner(*args,**kwargs):
#
#         dt = datetime.now(timezone.utc)
#         result = fn(*args,**kwargs)
#         print("at {0} for {1} ".format(dt,result))
#         return result
#     return inner
# def timer(fn):
#     from functools import wraps
#     from time import perf_counter
#     @wraps(fn)
#     def inner(*args,**kwargs):
#         start = perf_counter()
#         result = fn(*args,**kwargs)
#         end = perf_counter()
#         gap = end - start
#         print("for {0} in {1:.6f} {2}".format(fn.__name__,gap,result))
#         return result
#     return inner
#
# @logger
# @timer
# def fact(n):
#     from operator import mul
#     from functools import reduce
#     result = reduce(mul,range(1,n-1))
#     return result
#
# fact(10)


def memo(fact):
    cache = dict()

    def inner(n):
        if n not in cache\
                :
            cache[n] = fact(n)
        return cache[n]

    return inner

@memo
def fact(n):
    print("Calculating fact {0}!".format(fact(n)))
    return 1 if n < 2 else n * fact(n - 1)
print(fact(10))
# @memo
# def fibo(n):
#     print("calculating {0}".format(n))
#     return 1 if n < 3 else fibo(n - 1) + fibo(n - 2)
#
#
# print(fibo(10))


