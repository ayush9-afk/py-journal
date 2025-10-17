class Employee:
    language = "Python"#This is class attribute
    salary = 1200000

    def __init__(self, name, salary , language): #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


harry = Employee("Harry", 1300000, "JavaScript")
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)

'''
Teach by himanshu

class Employee:
   def __init__(self, id): # this is constructor and we define this to get rid of getters and setters
       self.id  = id
       print("new Employe have been created, and this is from constructor function")
       # print(self.id)

   def get_employee_id(self): # getters
       return self.id
    
       
e1 = Employee(121212121212121212121212)
e2 = Employee(563485485)
print(e1)
print(e2)

'''

# A constructor in Python is a special function that runs automatically when you create an object.