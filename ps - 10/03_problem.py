class demo:
    a = 4

o =demo()
print(o.a) #Prints the class attribute instant attibute is not present
o.a = 0 #Instant attribute is set
print(o.a) #Prints the instance attribute because instance attribute is present
print(demo.a) #Print class attribute
