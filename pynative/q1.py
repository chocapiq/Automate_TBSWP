#Question 1: Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum
a = int(input())
b = int(input())

if a * b > 1000:
    c = a + b
    print(c)
else:
    c = a * b
    print(c)
