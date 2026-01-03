from functools import reduce
a= [1,2,5,355645654,7654,7545,55]
l = [111, 2, 65, 53, 634, 65, 74, 45 , 55]

def grater(a, b):
    if (a>b):
        return a
    return b

print(reduce(grater, l))