try:
    age = int(input("Enter your age"))
    if age%2 == 0:
        print("Age is even")
    else:
        print("Age is odd")
except ValueError:
    print("Age should be in numbers")