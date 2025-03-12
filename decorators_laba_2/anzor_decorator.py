# Simple decorator
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@decorator
def say_hello(name):
    print(f"Hello, {name}")

say_hello("John")

# Decorate decorator
def sqr_log(func):
    def wrapper(*args, **kwargs):
        print("Начало работы.")
        result = func(*args, **kwargs)
        print(f"Результат после декоратора: {result}")
        print("Конец работы")
        return result
    return wrapper

def sqr_decorator(func):
    @sqr_log
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper
@sqr_decorator
def sum(a, b):
    return a + b

a = sum(12, 20)
print(a)

