class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 2

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 3

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructer of Manager")
    c = 4

#o = Employee()
#print(o.a) #Prints the a attribute

#o = Programmer()
#print(o.a, o.b)

o = Manager
print(o.a, o.b, o.c)
