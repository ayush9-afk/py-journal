#5! = 5 x 4 x 3 x 2 x 1

n = int(input("Enter the number: "))
product = 1
for i in range(1 ,1+n):
    product = product * i

print(f"Enter the factorial of {n} is {product}")