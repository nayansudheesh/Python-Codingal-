#ACP , Lesson  111 , "Biarry convesion"
decimal = int(input("Enter a whole number"))
original_decimal = decimal
binary = ""
while decimal >0:
    remainder = decimal%2
    binary = str(remainder) + binary
    decimal = decimal//2

print("binary number of" , original_decimal , "is" , binary)