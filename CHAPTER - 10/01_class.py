# class is empty 
# if something comes in class it's called an object
#
# Example:
# Ticket is empty → it's a class
# When someone’s identity is added → it becomes an object


class Employee:
    language = "Py"#This is class attribute
    salary = 1200000

# harry is an object

harry = Employee()
harry.name = "Harry"#This is an instance attribute
print(harry.name, harry.language, harry.salary)


rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is as instance attribute and salary and language are class attribute as they directely belong to the class