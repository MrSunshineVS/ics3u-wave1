from math import pi

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

radius = tryValue("Please enter cylinder radius")
height = tryValue("Please enter cylinder height")

print("{:.1f}".format(radius * radius * pi *  height))
