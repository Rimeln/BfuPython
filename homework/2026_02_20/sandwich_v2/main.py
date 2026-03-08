def bread(func):
    def wrapper():
        result = "Bread\n" + func() + "Bread"
        return result
    return wrapper

def salat(func):
    def wrapper():
        result = "Salat\n" + func()
        return result
    return wrapper

def tomato(func):
    def wrapper():
        result = "Tomato\n" + func()
        return result
    return wrapper

def meat(func):
    def wrapper():
        result = "Meat\n" + func()
        return result
    return wrapper

@bread
@salat
@tomato
@meat

def make_sandwich():
    return ""

print(make_sandwich())