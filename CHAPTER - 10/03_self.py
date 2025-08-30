class Employee:
    language = "Python"#This is class attribute
    salary = 1200000

    def set_name(self, name):
        self.name = name

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print(f"Good morning {self.name}")

emp1 = Employee()
emp1.set_name("Harry")
emp1.greet()
emp1.getInfo()
# Employee.getInfo(emp1) This is also Equivalent to the above line