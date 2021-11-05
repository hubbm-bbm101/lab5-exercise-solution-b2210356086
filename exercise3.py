print("This is a number guessing game, The interval is [1,100] (Both included)")
import random
target = random.randint(1,101)
guess = int(input("Please enter your guess: "))
while guess != target:
    if guess < target:
        guess= int(input("Increase your number: "))
    else:
        guess= int(input("Decrease your number: "))
print("Congratulations! The number is "+ str(target))
