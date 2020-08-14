# Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

list = []
lenList = int(input("Enter the length of the list.\n"))

for i in range(lenList):
    x = int(input("Enter the number for the list.\n"))
    list.append(x)
print("Divisible by 5 in the list:")
for i in list:
    if i%5 == 0:
        print(i)
