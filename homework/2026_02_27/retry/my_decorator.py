def retry(count):
    def decorator(func):
        def wrapper():
            attempts = count
            while attempts > 0:
                try:
                    return func()
                except ValueError:
                    attempts -= 1
                except OSError:
                    print(f"{func.__name__} raise OsError exception.")
                    attempts -= 1
        return wrapper
    return decorator
