import random
n = random.randint(1,100)
a = -1
guesses = 0
while (a !=n):
    guesses +=1
    a = int(input("Guess the number is: "))
    if(a >n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number please")
        guesses +=1

print(f"You have guesses the number {n} correctly in {guesses} attempts")