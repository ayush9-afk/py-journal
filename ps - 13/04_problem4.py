def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,5,355645654,7654,7545,55]

f = list(filter(divisible5, a))
print(f)