import functools
import time

def Time(func):
    @functools.wraps(func)
    def wrapper_time(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        ran = end - start
        print("Finished {func.__name__!r} in {ran:.20f} secs".format(
            func=func, ran=ran))
        return value
    return wrapper_time

@Time
def LinealSearch(array: list, target: int) -> int:
    for x in range(len(array)):
        if array[x] == target:
            return x

@Time
def TransversalSearch(array: list, target: int) -> int:
    for x in range(len(array)):
        if array[x] == target:
            return x
        if array[x*-1] == target:
            return x*-1

array = range(0, 10000)

print(LinealSearch(array, 1.5))
print(TransversalSearch(array, 9))

print(LinealSearch(array, "Hola"))
