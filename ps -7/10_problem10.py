#n = int(input("Enter the number: "))
#for i in range(1 , 11):
#    print(f"{n} * {i} = {n*i}")

#reversed multiplication
'''
   1  10  =11
   2  9   =11
   3  8   =11
   4  7   =11
   .  .    
'''

n = int(input("Enter the number: "))
for i in range(1 , 11):
    print(f"{n} * {11-i} = {n*(11-i)}")