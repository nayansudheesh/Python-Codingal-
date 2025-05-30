import random
playing = True

print("I will generate a number from 1 to 10, try to guess that number 1 digit at a time.")
print("Game ends when your guess is correct.")
number = random.randint(1,10)
guess = int(input("Enter any number(not in words!)"))
if guess == number:
    print("Your guess is correct")
    print("The number was" ,number)
else:
    print("The guess is not correct , try again.")