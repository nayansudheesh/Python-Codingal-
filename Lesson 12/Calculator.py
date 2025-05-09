def add( x , y):
   return x + y
def subtract( x , y):
   return x-y
def multiply(x,y):
   return x*y
def divide(x,y):
   return x/y
print("Choose the following operations")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. divide")

choice = input("Enter your choice (a/b/c/d)")
x = int(input("Enter first number"))
y = int(input("Enter 2nd number."))

if choice == 'a':
   print(x , "+" , y , "=", add(x , y))
if choice == 'b':
   print(x , "-" , y , "=", subtract(x , y))
if choice == 'c':
   print(x , "x" , y , "=", multiply(x , y))
if choice == 'd':
   print(x , "/" , y , "=", divide(x , y))
else:
   print("This is invalid , please enter (a/b/c/d)")