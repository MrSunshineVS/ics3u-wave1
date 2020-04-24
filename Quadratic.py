from math import sqrt

# sign is either 1 or -1
def UseQuadratic(a, b, discr, sign):
    return (-b + (sign * sqrt(discr))) / (2*a)

a = 0
b = 0
c = 0

# get input
print("Enter values:")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

# print finished quadratic equation:
print("f(x) = {0}x\u00b2 + {1}x + {2}\n".format(a, b, c))

# find number of zeros
discriminant = b**2 - 4*a*c

# find number of roots
nRoots = 2
if(discriminant < 0): nRoots = 0
elif(discriminant == 0): nRoots = 1

print("Number of roots: {0}".format(nRoots))

if(nRoots > 0):
    print("x = {:f}".format(UseQuadratic(a, b, discriminant, 1)))
    if(nRoots > 1):
        print("x = {:f}".format(UseQuadratic(a, b, discriminant, -1)))
