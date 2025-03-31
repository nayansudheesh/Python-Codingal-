age = 35
weight = 39.34
is_student = False
name = "Penguin"

print("Datatype of age is:" , type(age))
print("Datatype of weight is:" , type(weight))
print("Datatype of is student is:" , type(is_student))
print("Datatype of name is:" , type(name))

# After casting
age = str(age)
weight = int(weight)
is_student = float(is_student)
name =  bool(name)

print(age)
print("Datatype of age is:" , type(age))
print(weight)
print("Datatype of weight is:" , type(weight))
print(is_student)
print("Datatype of is student is:" , type(is_student))
print(name)
print("Datatype of name is:" , type(name))