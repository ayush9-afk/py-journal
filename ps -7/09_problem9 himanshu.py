'''

* * *
*   *   n = 3
* * *

'''
import time
n = int(input("Enter the number: "))
print(f"Creating ({n} x {n}) square......")
time.sleep(3)
for i in range(1 ,n+1):
    if(i==1 or i==n):
        print(" - "* n)
  
    elif i == n/2:
        print("   "*(int((n-2)/2)), end="")
        print("K", end = "")
        print(" * ")

    else:
     print(" - ", end="")
     print("   "*(n-2), end="")
     print(" - ", end="")
     print("", end = "\n")