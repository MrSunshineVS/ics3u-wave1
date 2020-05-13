def FindPrime(num):
    if(num <= 1):
        return False
    i = 2
    while(num > i):
        if num % i == 0:
            return False
        i += 1
    return True

def main():
    value = int(input("Enter value: "))
    if(FindPrime(value)):
        print("This value IS a prime number.")
    else:
        print("this value IS NOT a prime number.")

if __name__ == '__main__':
    main()
