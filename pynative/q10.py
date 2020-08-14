# Question 10: Given a two list of numbers create a new list
# such that new list should contain only odd numbers from the first list and even numbers from the second list

ListA = [10, 20, 23, 11, 17]
ListB = [13, 43, 24, 36, 12]
ListC = []
for i in ListA:
    if i%2 == 1:
        ListC.append(i)
for i in ListB:
    if i%2 == 0:
        ListC.append(i)
print(ListC)