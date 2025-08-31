class Employee:
    language = "Python"#This is class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    def update_salary(self, salary):
        self.salary = salary

    # def greet(self):
    #     print(f"Good morning")

emp1 = Employee()
# emp1.getInfo()
Employee.getInfo(emp1) # This is also Equivalent to the above line
emp1.update_salary(2000000)
Employee.getInfo(emp1) # This is also Equivalent to the above line