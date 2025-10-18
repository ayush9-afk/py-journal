class Employee:
    a = 1
    
    @classmethod 
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property # get value
    def name(self):
        return f"{self.name} {self.lname}"
    
    @name.setter # set value (with control or validation)
    def name (self, value):
        self.fname = value.split(" ")[0]   
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Harry Khan"
print(e.fname, e.lname)

e.show()

# Encapsulation - Hiding data and controlling access   
# Abstraction - Hiding unnecessary details