class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of employee {self.name} and the company is {self.company}")


class coder:
        language = "Python"
        def printLanguages(self):
             print(f"Out of all language here is your language {self.language}")

class Programmer(Employee, coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()