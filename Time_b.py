def tryValue(message):
    while(True):
        try:
            value = int(input(message + ": "))
        except ValueError:
            print("That is not a valid value, try again.")
            continue

        if(value < 0):
            print("This value is negative, try again.")
        else:
            return value

def tryTime(secsLeft, timeVal, format=":02d"):
    string = "{"+format+"}"
    timeCount = secsLeft // timeVal
    print(string.format(timeCount), end ='')
    return secsLeft - timeCount * timeVal

nMinuteSecs = 60               # seconds in a minutes
nHourSecs = 60 * nMinuteSecs   # seconds in an hour
nDaySecs = 24 * nHourSecs      # seconds in a day

nTimeVals = [nDaySecs, nHourSecs, nMinuteSecs, 1]

nTotalSeconds = tryValue("Number of seconds")

nTotalSeconds = tryTime(nTotalSeconds, nDaySecs, "0")
for i in range(1, len(nTimeVals)):
    print(':', end='')
    nTotalSeconds = tryTime(nTotalSeconds, nTimeVals[i])
