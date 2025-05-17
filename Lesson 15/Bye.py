valid = False

while not valid:
    try:
        n = int(input("enter any number"))
        while n%2 == 0:
             print("Bye")
             valid = True
    except ValueError:
        print("Invalid")