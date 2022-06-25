def add(x, y):
    return x * y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 2
b = 3

print(do_twice(add, a, b))


# So cool things
