print("To enter this class , you must be above 10 years old and less than 20 yrs old")
age = int(input("Enter your age in numbers(21 , 22 , etc)"))
if (age >= 10 and age <=20 ):
    print("You are eligble for the exam")
else:
    print("You are not eligble for the exam")
    print("You are " , age , "Years old , you must be greater than 10 but less than 20 years old.")