# Exercise Question 3: Convert decimal number to octal using print() output formatting

input = int(input("Enter the number"))

print("It's octal value is " + oct(input))

#alternative
print("%o" % (input))