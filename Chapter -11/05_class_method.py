class Employee:
    a = 1
    @classmethod # this will print class value
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()