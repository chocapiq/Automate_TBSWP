# Exercise Question 4: Display float number with 2 decimal places using print()
input = float(input("Enter the number with 2 or more decimals to round it."))

print(round(input, 2))

# alternative
print("%.2f" % input)