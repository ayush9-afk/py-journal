class Employee:
    language = "Python"#This is class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

#    def greet(self):
#        print(f"Good morning")
    
#    def get_joining_date(self):
#        return self.joinoing_date
    
#    def set_joining_date(self, joining_date: str):
#        self.joinoing_date = joining_date
    

harry = Employee()
harry.language = "JavaScript" # This is an instance attribute
#harry.set_joining_date("9th August 2006")
#print(harry.get_joining_date())
#harry.greet()#harry.getInfo()
Employee.getInfo(harry)
