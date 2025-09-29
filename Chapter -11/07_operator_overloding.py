class Number:

    def __init__(self, n):
        self.n = n   # assign instance variable
    
    def __add__(self, num):
        return self.n + num.n
    
n = Number(1)
m = Number(5)

print(n + m)