import random
n=random.randint(1,100)
a = -1
guesses = 0
while (a != n):
    a = int(input("Guess the Number: "))
    if(a>n):
        print("Lower  number please")
        guesses +=1
    elif(a<n):
        print("Higher number please")
        guesses +=1

print(f"you have guess the number {n} corectly in {guesses} attempts")
