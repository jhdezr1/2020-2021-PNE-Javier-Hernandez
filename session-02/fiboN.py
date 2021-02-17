def fibon(n):
    x = 0
    y = 1
    for i in range(0, n - 1):
        fn = x + y
        x = y
        y = fn
    return fn

print('5th fibonacci term: ', fibon(5))
print('10th fibonacci term: ', fibon(10))
print('15th fibonacci term: ', fibon(15))