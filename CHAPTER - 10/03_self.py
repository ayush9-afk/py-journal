class Employee:
    language = "Python"#This is class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod  # A method that doesn’t use self or cls.
    def greet():
        print("Good morning")


harry = Employee()
# harry.language = "JavaScript" # This is an instance attribute
harry.getInfo()
# Employee.getInfo(harry)