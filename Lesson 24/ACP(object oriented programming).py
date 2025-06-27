#ACP

class dog:

    def __init__(self, breed , age , name):
        self.breed = breed
        self.age = age
        self.name = name

dog1 = dog( "indian" , 4 , "max")
print("{} is of {} breed and is {} years old".format(dog1.name , dog1.breed , dog1.age ))
dog2 = dog("australian" , 5 , "daniel")
print("{} is of {} breed and is {} years old".format(dog2.name , dog2.breed , dog2.age ))
dog3 = dog("american" , 8 , "clark")
print("{} is of {} breed and is {} years old".format(dog3.name , dog3.breed , dog3.age ))