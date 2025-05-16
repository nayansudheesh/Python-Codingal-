def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
num = int(input("Enter any number"))
if num < 0:
    print("Factorial cannot be found for numbers lesser than 0")
else:
    print(f"the factorial for {num} is {factorial(num)}")
    