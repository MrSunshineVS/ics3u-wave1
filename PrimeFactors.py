def tryValue(message):
    while(True):
        try:
            tryValue = int(input(message + ": "))
        except ValueError:
            print("That is not a valid value, try again.")
            continue

        if(tryValue < 2):
            print("This value is less than 2, try again.")
        else:
            return tryValue

def FindFactors(num):
    factor = 2
    while(factor <= num):
        if(num % factor == 0):
            print(factor)
            num //= factor
        else:
            factor += 1

def main():
    value = tryValue("Please enter value")
    FindFactors(value)

if __name__ == '__main__':
    main()
