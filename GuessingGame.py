import random

print("Number Guessing Game")
number=random.randint(1,9)
chances=0
print("Guess the number between 1 and 9")
while chances<5:
     guess=int(input("Enter your guess : "))
     if guess==number:
          print("Congratulations! You won the game")
          break
     elif guess<number:
          print("your guess is too low. please guess a number higher than ",guess)
     else:
          print("your guess is too high. please guess a number lower than ",guess) 
     chances+=1

if not chances<5:
        print("You lose...the correct number was ",number)
              