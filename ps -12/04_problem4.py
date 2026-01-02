try:
    a =int(input("Enter first number:"))
    b =int(input("Enter first number:"))
    print(a/b)
except ZeroDivisionError:
    print("Infinite")