import random

nRed = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

# we use negative one for 00
nRoll = random.randrange(-1, 37)

if nRoll > 0:
    print("The spin resulted in {0}...".format(nRoll))

    # Part 1
    print("Pay {0}".format(nRoll))

    # Part 2
    if nRoll in nRed:
        print("Pay Red")

    else:
        print("Pay Black")

    # Part 3
    if nRoll % 2 == 0:
        print("Pay Even")
    else:
        print("Pay Odd")

    # Part 4
    if(nRoll < 19):
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")

else:
    sZeros = "0"
    if(nRoll < 0):
        sZeros += "0"

    print("The spin resulted in " + sZeros + "...")
    print("Pay ", sZeros)
