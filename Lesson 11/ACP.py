#ACP , "Mirrored triangle" , lesson 112.
rows = int(input("enter number of rows"))

for i in range(1 , rows +1):
  spaces = rows = i
  sign = i
  print("" * spaces + "+" * sign)
