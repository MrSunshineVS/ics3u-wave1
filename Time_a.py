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

nDays = tryValue("Number of days")
nHours = tryValue("Number of hours")
nMinutes = tryValue("Number of minutes")
nSeconds = tryValue("Number of seconds")

nMinuteSecs = 60               # seconds in a minutes
nHourSecs = 60 * nMinuteSecs   # seconds in an hour
nDaySecs = 24 * nHourSecs      # seconds in a day

nTotalSeconds = nDaySecs * nDays + nHourSecs * nHours + nMinuteSecs * nMinutes + nSeconds

print("Total seconds: {0}".format(nTotalSeconds))
