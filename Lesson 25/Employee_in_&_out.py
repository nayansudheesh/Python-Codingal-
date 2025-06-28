class Employee:
    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructor called")
    
def Create_obj():
        print("Currently making object...")
        obj = Employee()
        print("Function ended...")
        return obj
print("Calling creatobj() function...")
obj = Create_obj()
print("Program has ended...")