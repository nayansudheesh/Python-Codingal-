q1 = input("What causes summer?")
if q1 ==("The tilt of the earth towards the sun") :
 print("Correct!")
 score = 1
else:
    print("False! correct ans is:The tilt of the earth towards the sun")
    score = 0
q2 = input("When does summer start?(India)")
if q2 == ("Around april") or ("Arround April") :
    print("Correct!")
    score = score + 1 
else:
    print("False , correct ans is:Around april ")
    score = score - 1
print("Your score is:" , score)