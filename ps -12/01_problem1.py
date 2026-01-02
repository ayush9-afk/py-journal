try:
    with open ("1.text", "r") as f:
        print(f.read())
except Exception as e:
        print(e)
try:
    with open ("2.text", "r") as f:
        print(f.read())
except Exception as e:
        print(e)        
try:
    with open ("3.text", "r") as f:
        print(f.read())
except Exception as e:
        print(e)

print("Thank You!")
