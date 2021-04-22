print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill ? $"))
precentage = float(input("What precentage tip would you like to give? 10, 12, or 15?"))
people = float(input("How many people to split the bill?"))

result = (total_bill / people) * ((100 + precentage) / 100)
print("Each person should pay: ${:.2f}".format(result))
