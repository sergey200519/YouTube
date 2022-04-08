# a, *b, c = ["a", True, 3, 4, 5, 6]
# print(c)
# print(b)
# print(a)
# a = [1, 9]
# print(list(range(a)))
# print(*a)


# def f(*args, **kwargs):
#     return f"{args}\n{kwargs}"
# print(f(1, "2", True, [1, 2], a="a", b="b", c=1))

# def f(*args, **kwargs):
#     for item in args:
#         print(item)
#
# f(1, "2", True, [1, 2], a="a", b="b", c=1)
# print("---------------------------------------")
# def f(*args, **kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print(f(1, "2", True, [1, 2], a="a", b="b", c=1))



from datetime import datetime

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper




@timeit

pass

def f(n, t):
    num = 0
    for i in range(n):
        num += i

    return num + t

print(f(90000, t=100))
