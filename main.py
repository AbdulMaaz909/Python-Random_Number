# write a program that generates  as random number and asks the users to guess it.
# if the player's guess is higher than the actual number, then 
# program displays "lower number please".Similarly if the user guess is too low,the program prints "Higher number please" When the user guess
#the correct number,the program display the number of guesses the player used to arrive at the number

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