from functools import reduce
# Map Example
l = [1, 2, 3, 4, 5]

squared = lambda x: x*x

sqList = map(squared, l)
print(list(sqList))

# Filter Example
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Example
def sum(a, b):
    return a +b

mul = lambda a,b : a*b
print(reduce(sum, l))
print(reduce(mul, l))