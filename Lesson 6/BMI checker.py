height = float(input("Enter your height in cm"))
weight = float(input("Enter your weight in KG`s"))
bmi = weight / (height/100)**2
print("Your BMI(Body Mass Index) is:" , bmi)

if bmi <= 18.4 : print("You are underweight")

elif bmi <= 24.9 : print("You are healthy")

elif bmi <= 29.9 : print("You are over-weight")

elif bmi <= 34.9 : print("You are severly over-weight")

elif bmi <= 39.9 : print("You are obese")
else:
    print("You are severly obese")