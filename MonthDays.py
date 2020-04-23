sMonth = str(input("Please enter month name: "))

# We use the short versions because they are part of the larger words
# plus it is harder to not get your answer if you spelled the month incorrectly,
# which is just frustrating.
sMonthNames = ["Jan", "Feb", "Mar",
               "Apr", "May", "Jun",
               "Jul", "Aug", "Sep",
               "Oct", "Nov", "Dec"]

sMonthDays = ["31", "28 or 29", "31",
              "30", "31", "30",
              "31", "31", "30",
              "31", "30", "31"]

nMonth = -1
for i in range(12):
    if (sMonth[:3].lower() == sMonthNames[i].lower()):
        nMonth = i
        break;

print(sMonthDays[nMonth], "days.")
