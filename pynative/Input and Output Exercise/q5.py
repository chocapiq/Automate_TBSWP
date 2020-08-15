# Exercise Question 5: Accept list of 5 float numbers as a input from user
lenList = int(input("How many numbers you want to put in a list? \t"))
list = []

for i in range(lenList):
    b = float(input())
    list.append(b)

print(list)