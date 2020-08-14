# Question 2: Given a range of first 10 numbers,
# Iterate from start number to the end number and print the sum of the current number and previous number
for i in range(10):
    if i <= 0:
        n = 0
    else:
        n = i - 1
    print("Current Number " + str(i) + " Previous Number " + str(n) + " Sum: " + str(i+n))