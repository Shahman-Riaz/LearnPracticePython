# def foo(*args):
#     avg = sum(args)/len(args)
#     return avg

# print(foo(2, 3, 5, 7))


def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)
print(foo('good', 'bad', 'ass', 'bat'))