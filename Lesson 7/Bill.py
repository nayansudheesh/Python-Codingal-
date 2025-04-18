unit = int(input("Enter the units of electricity you have used"))
if (unit <= 50) :
    amount = unit * 2.60
    tax = 25
elif ( unit <= 100):
     amount = 120 + ((unit - 50) * 3.90)
     tax = 40
elif (unit <= 200):
     amount = 140 + ((unit - 100)*5.25)
     tax = 60
else:
 amount = 153 + ((unit - 200)*8.45)
 tax = 70
total = amount + tax
print("Electricity bill is: ₹" , total)