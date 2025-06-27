class parrot:

    def __init__(self, name,species , age):
        self.name = name
        self.species = species
        self.age = age

blu = parrot("blu" , "bird" , 15)
woo = parrot("woo" , "bird" , 10)

print("Blu is a {}".format(blu.species))
print("Woo is a {}".format(woo.species))

print("{} is  {} years old".format(blu.name ,blu.age))
print("{} is  {} years old".format( woo.name , woo.age))