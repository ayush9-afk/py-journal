'''
For n=3
  *
 ***  
*****


for n=5
    *
   ***  
  ***** 
 ********
**********   

'''

n= int(input("Enter the number: "))
for i in range(1 , n+1):
    print(" "* (n-1), end="")
    print("*"*(2*i - 1), end="")
    print("")
