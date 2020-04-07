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

sqftToAcres = 43560

width = tryValue("Please enter farm width")
height = tryValue("Please enter farm height")

print("{:.2f}".format((width * height) / sqftToAcres))
