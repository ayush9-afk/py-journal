marks = {
    "Harry":100,
    "Shubham":56,
    "Rohan":63
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry":99, "Kalash":98})
print(marks)

print(marks.get("Harry")) #Prints none
print(marks["Harry"])  #Returns error
