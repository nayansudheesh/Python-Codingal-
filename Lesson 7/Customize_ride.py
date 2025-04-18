print("Select your ride:")
print("1. Car")
print("2. Bike")
choice1=int(input("Enter your choice(number 1 or 2)"))

if (choice1 == 1):
    print("You have chosen car")
    print("What type of car?")
    print("1. XUV")
    print("2. Sedan")
    choice2 = int(input("Enter your choice"))
    if(choice2 == 1):
      print("You have chosen XUV")
    else:
      print("You have chosen Sedan")
elif(choice1 == 2):
    print("You have chosen bike")
    print("What type of bike?")
    print("1. Scooter")
    print("2.Scooty")
    choice3 = int(input("Enter your choice"))
    if (choice3 == 1):
     print("You have chosen scooter")
    else:
     print("You have chosen scooty.")

