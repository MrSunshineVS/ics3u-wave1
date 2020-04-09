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


# Need failsafe for pennies (singular: pennY, plural: pennIES)
def UseCoin(change, coinValue, coinName):
    coinCount = change // coinValue
    if (coinCount > 0):
        multipliedName = coinName
        if(coinCount > 1):
            if(coinName == "Penny"):
                multipliedName = "Pennies"
            else:
                multipliedName += 's'

        print("{0} ".format(coinCount) + multipliedName)

    return change - (coinCount * coinValue)


# 2d array for coin values and names
aCoins = [
    ["Toonie",   200],
    ["Loonie",   100],
    ["Quarter",  25],
    ["Dime",     10],
    ["Nickel",   5],
    ["Penny",    1]
]

nChange = tryValue("Please enter your change")

if(nChange == 0):
    print("You don't need change. Goodbye!")
else:
    for i in range(len(aCoins)):
        nChange = UseCoin(nChange, aCoins[i][1], aCoins[i][0])
