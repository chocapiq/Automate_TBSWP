# Question 11: Write a code to extract each digit from an integer, in the reverse order

n = int(input("Enter the number\n"))
x = str(n)[::-1]
list = list(x)
for i in list:
    print(i, end=" ")