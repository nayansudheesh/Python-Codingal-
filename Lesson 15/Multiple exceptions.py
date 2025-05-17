try:
    num1 = int(input("Enter any number"))
    num2 = int(input("Enter another number"))
    result = num1/num2
    print("The result is " , result)
except ZeroDivisionError:
    print("Divison by zero is not allowed")
except ValueError:
    print("Please enter any number , not words")
except NameError as ex:
    print("The exception is" , ex)
except:
    print("Some error has occured")
finally:
    print("This will always execute")