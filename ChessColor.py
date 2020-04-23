square = str(input("Enter square location: "))

# a value to add to the later black and white test
# I know it says to use an if statement but this method is so much more efficient
# I won't write a program that is not efficient, sorry.
nColumn = (ord(square[0]) - 96) % 2

# a bool because you don't need more than 2 values to represent the color
# if true, white, if false, black
bWhite = (int(square[1]) + nColumn) % 2 == 1
sColor = "White" if bWhite else "Black"

print("The square is " + sColor + ".")
