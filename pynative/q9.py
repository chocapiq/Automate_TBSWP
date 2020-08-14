# Question 9: Reverse a given number and return true if it is the same as the original number
n = int(input("Enter the number\n"))
x = str(n)[::-1]
if str(n) == x:
    print("Original number is " + str(n))
    print("The original and reverse number is the same")
else:
    print("Original number is " + str(n))
    print("The original and reverse number is not same")