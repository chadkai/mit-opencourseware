# Inputs
annualSalary = float(input("Input your current annual salary; "))

# Defined variables
semiAnnualRaise = .07
currentSavings = 0
r = 0.04/12
month = 0

# Counter
steps = 0

# Bisection method to find savings rate
lowRate = 0.0
highRate = 1.0
guessRate = (highRate+lowRate)/2

# Assigning values to the variables I need
downPayment = 250000
monthlySalary = annualSalary/12

found = False

while abs(currentSavings - downPayment) >= 100.0:
    # Establishing variable
    monthlyAmountSaved = monthlySalary * guessRate
    # While loop to find total current savings under the current guessRate iteration
    while month < 36:
        currentSavings = (currentSavings + monthlyAmountSaved) * (1 + r)
        month += 1
        if month % 6 == 0:
            monthlyAmountSaved = monthlyAmountSaved * (1 + semiAnnualRaise)

    # Bisection
    if currentSavings < downPayment:
        lowRate = guessRate
    else:
        highRate = guessRate

    # Counter
    steps += 1

    # Breaking loop when currentSavings is in range or when it is not possible to save
    if int(currentSavings) in range(249900, 250100):
        break
    elif steps == 36:
        print("Not possible to save with your current salary.")
        break

    # Resetting values
    currentSavings = 0
    month = 0
    guessRate = (highRate + lowRate) / 2
    # Adding steps to the counter

print("Recommended savings rate: ", guessRate)
print("Number of steps in bisection method: ", steps)
print(steps)
