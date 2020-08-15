# Question 13: Print multiplication table form 1 to 10

for i in range(1, 11):
    for j in range(1, 11):
        k = i*j
        print(k, end=" ")
    print("\t\t")
