class Employee:
    language = "Py"#This is class attribute
    salary = "1200000"


harry = Employee() # Harry ab 'Employee' class ka Object hai

harry.language = "JavaScript"#This is an instance attribute
print(harry.language, harry.salary)
#print(type(harry))
#print(harry)