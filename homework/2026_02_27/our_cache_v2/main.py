import os

def cache(file, key_type="pos"):
    def decorator(func):
        cache_st = {}

        if os.path.exists(file):
            with open(file, "r") as f:
                for line in f:
                    key, value = line.strip().split("|")
                    cache_st[key] = value

        def wrapper(*args, **kwargs):
            if key_type == "pos":
                key = str(sorted(args))
            elif key_type == "named":
                key = str(sorted(kwargs.items()))

            if key in cache_st:
                return cache_st[key]

            result = func(*args, **kwargs)
            cache_st[key] = result

            with open(file, "a") as f:
                f.write(f"{key}|{result}\n")
            return result
        return wrapper
    return decorator


@cache("cache.txt","pos")
def my_sum(a, b):
    print("---")
    return a + b

print(my_sum(1,2))
print(my_sum(1,2))

print(my_sum(3,2))
print(my_sum(2,1))
print(my_sum(1,2))