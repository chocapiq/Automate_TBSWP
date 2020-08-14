# Question 12: Calculate income tax for the given income by adhering to the below rules
n = int(input("Enter the number to calculate tax.\n"))

if n <= 10000:
    n = n
    i = 0
    tax = i
elif n <= 20000:
    i = n - 10000
    i = i*0.1
    n = n + 1
    tax = i
elif n > 20000:
    i = n - 10000
    j = i - 10000
    i = i * 0.1
    j = j * 0.1
    n = n + i + j
    tax = i + j
print("Income tax is " + str(tax) + "zł")