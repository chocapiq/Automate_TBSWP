# Question 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
numA = int(input("Enter the base number \t"))
numB = int(input("Enter the number to exponent \t"))


def exponent(base, exp):
    i = 1
    while i < exp:
        base = base * numA
        i += 1
    print(str(numA) + " raised to the power of " + str(numB) + " is: " + str(base))
exponent(numA, numB)