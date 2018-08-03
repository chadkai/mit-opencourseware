# Inputs
annualSalary = 300000

# Defined variables
semiAnnualRaise = .07
currentSavings = 0
r = 0.04/12
month = 0
epsilon = 100

# Counter
steps = 0

# Bisection method to find savings rate
lowRate = 0.0
highRate = 1.0
guessRate = (highRate+lowRate)/2

# Assigning values to the variables I need
downPayment = 250000
monthlySalary = annualSalary/12

while abs(currentSavings - downPayment) > epsilon:
    monthlyAmountSaved = monthlySalary * guessRate
    while month < 36:
        currentSavings = (currentSavings + monthlyAmountSaved) * (1 + r)
        month += 1
        if month % 6 == 0:
            monthlyAmountSaved = monthlyAmountSaved * (1 + semiAnnualRaise)
    print(currentSavings)
    if currentSavings < downPayment:
        lowRate = guessRate
    else:
        highRate = guessRate
    currentSavings = 0
    month = 0
    guessRate = (highRate + lowRate) / 2
    steps += 1
    if steps == 36:
        break
    print(guessRate)
