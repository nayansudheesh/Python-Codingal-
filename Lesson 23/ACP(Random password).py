#ACP , Lesson  125 , "random password challenge"
import random
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' ,'z' ]
uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
randompassword = ""
for i in range (6):
    random_int = str(random.randint(1 , 10))
    random_lowercaseletter = random.choice(lowercase_letters)
    random_uppercaseletter = random.choice(uppercase_letters)
    randompassword += (random_int+random_lowercaseletter+ random_uppercaseletter)

print("Your random password is:" , randompassword) 