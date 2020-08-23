# Print data with inputs
import math
totalMoney = int(input("How much money do you have? "))
price = int(input("What's the price of the item you want to buy? "))
item = input("What's the name of the item? ")
quantity = math.floor(totalMoney/price)
print("You have " + str(totalMoney) + " zloty so you can buy " + str(quantity) + " " + str(item) + " for " + str(price) + " each.")