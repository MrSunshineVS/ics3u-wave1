from time import time

nMinuteSecs = 60               # seconds in a minutes
nHourSecs = 60 * nMinuteSecs   # seconds in an hour
nDaySecs = 24 * nHourSecs      # seconds in a day
nYearSecs = int(365.24 * nDaySecs)

sMonthNames = ["Jan", "Feb", "Mar",
               "Apr", "May", "Jun",
               "Jul", "Aug", "Sep",
               "Oct", "Nov", "Dec"]

nMonthDays = [31, 28, 31,
              30, 31, 30,
              31, 31, 30,
              31, 30, 31]

sWeekNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

nTotalSeconds = int(time()) + 1970 * nYearSecs

# Convert to Eastern Digital Time (from UTC)
nTotalSeconds -= 4 * nHourSecs

# Get weekday (epoch was on a thursday)
nWeekDay = ((nTotalSeconds // nDaySecs) + 4) % 7

# Get year value
nYears = nTotalSeconds // nYearSecs
nTotalSeconds -= nYears * nYearSecs

# Get month value
nMonths = 0
nDays = 0
for i in range(12):
    nMonthSecs = (nDays + nMonthDays[i]) * nDaySecs
    if(nTotalSeconds // nMonthSecs > 0):
        nDays += nMonthDays[i]
    else:
        nMonths = i
        break

nTotalSeconds -= nDays * nDaySecs

# Get day value
nDays = nTotalSeconds // nDaySecs
nTotalSeconds -= nDays * nDaySecs

# Get hour value
nHours = nTotalSeconds // nHourSecs
nTotalSeconds -= nHours * nHourSecs

# Get minute value
nMinutes = nTotalSeconds // nMinuteSecs
nTotalSeconds -= nMinutes * nMinuteSecs

# Get second value
nSeconds = nTotalSeconds

# Construct string
datetime = "{0} {1} {2} {3:02d}:{4:02d}:{5:02d} {6}".format(sWeekNames[nWeekDay], sMonthNames[nMonths], nDays, nHours, nMinutes, nSeconds, nYears)
print(datetime)
