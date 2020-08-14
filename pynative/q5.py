# Question 5: Given a list of numbers, return True if first and last number of a list is same

list = []
lenList = int(input("Enter the length of the list.\n"))

for i in range(lenList):
    x = int(input("Enter the number for the list.\n"))
    list.append(x)
print("Given list is " + str(list))
print("result is " + str(bool(list[0] == list[-1])))
