marks = int(input("Enter your marks:"))

if(marks<=100 or marks>=90):
    grade = "Ex"
elif(marks<90 or marks>=80):
    grade = "A"
elif(marks<80 or marks>=70):
    grade = "B"
elif(marks<70 or marks>=60):
    grade = "C"
elif(marks<60 or marks>=50):
    grade = "D"
elif(marks>50):
    grade = "F"

print("Your garade is:", grade)