medical_cause = bool(input("Do you have a medical causes?(Enter boolean 'True' or 'False')"))
attendance = int(input("Enter total days of attendance"))
if (medical_cause == True) :
        print("You are allowed for exam")
else:
  if (attendance >= 75) :
        print("You are allowed for the exam")
  else:
        print("You cannot go for the exam")