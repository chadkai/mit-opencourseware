# Inputs
annualSalary = float(input("Enter your annual salary: "))
portionSaved = float(input("Enter the percent of your salary to save, as a decimal: "))
totalCost = float(input("Enter the cost of your dream home: "))

# Initializing values
portionDownPayment = 0.25
currentSavings = 0
r = 0.04
r2 = r/12

# Counter
months = 0

# Assigning values to the variables I need
downPayment = totalCost * portionDownPayment
monthlySalary = annualSalary/12
monthlyAmountSaved = monthlySalary * portionSaved

while currentSavings < downPayment:
    currentSavings = (currentSavings + monthlyAmountSaved)*(1 + r2)
    months += 1

print("Number of months: ", months)
