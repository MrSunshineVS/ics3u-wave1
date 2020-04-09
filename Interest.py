def tryValue(message):
    while(True):
        try:
            tryValue = int(input(message + ": "))
        except ValueError:
            print("That is not a valid value, try again.")
            continue

        if(tryValue < 0):
            print("This value is negative, try again.")
        else:
            return tryValue

def updateYear(balance, interest, message):
    balance *= (1.0 + interest)
    print(message + ": " + "{:.2f}".format(balance))
    return balance

nBalance = tryValue("Please enter the initial balance")

# First year
nBalance = updateYear(nBalance, 0.04, "First year")

# Second year
nBalance = updateYear(nBalance, 0.04, "Second year")

# Third year
nBalance = updateYear(nBalance, 0.04, "Third year")
