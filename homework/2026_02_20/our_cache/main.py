def cache(func):
    cache_st = {}
    def wrapper(*args):
        if args in cache_st:
            return cache_st[args]

        result = func(*args)
        cache_st[args] = result
        return result
    return wrapper

@cache
def my_sum(a, b):
    print("---")
    return a + b

print(my_sum(1, 2))
print(my_sum(2, 3))
print(my_sum(1, 2))
print(my_sum(2, 3))
print(my_sum(2, 3))
print(my_sum(2, 4))
