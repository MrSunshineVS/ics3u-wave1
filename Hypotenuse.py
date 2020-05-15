from math import sqrt

def ComputeHypotenuse(sideA, sideB):
    return sqrt(sideA**2 + sideB**2)

def main():
    sideA = float(input("Please enter first side length: "))
    sideB = float(input("Please enter second side length: "))
    print("The hypotenuse is: {:.2f}".format(ComputeHypotenuse(sideA, sideB)))

if __name__ == '__main__':
    main()
