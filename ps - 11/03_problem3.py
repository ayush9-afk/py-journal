class Employee:
    salary = 234
    incriment = 20
    @property
    def salaryAfterIncriment(self):
        return (self.salary + self.salary * (self.incriment)/100)   

    @salaryAfterIncriment.setter 
    def salaryAfterIncriment(self, salary):
        self.incriment = ((salary/self.salary) -1)*100



e = Employee()
#print(e.salaryAfterIncriment)
e.salaryAfterIncriment = 280.8
print(e.incriment)