class Employee:
    a = 1
    
    @classmethod # method that acts on the class, not the object.
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()