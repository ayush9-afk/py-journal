class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Harry", 2300000, 245001)
print(p.name, p.salary, p.pin, p.company)

#Done by me
# class programmer:
#     company = "Microsoft"
#     salary = 20000000

#     def __init__(self, name, salary, post):
#         self.name = name
#         self.salary = salary
#         self.post = post  
#         print("New joining in Microsoft company")

#     def employee(self):
#         print(f"Company name is Microsoft {self.name}. salary is {self.salary}.Mnber post is {self.post} ")

# ayush = programmer("Harry", 2000000, "HR")
# print(ayush.name, ayush.salary, ayush.post)
# programmer.employee(ayush)
