def ShippingCharge(items):
    firstItemShipped = False;
    charge = 0;
    for i in range(items):
        if(firstItemShipped):
            charge += 2.95;
        else:
            charge += 10.95;
            firstItemShipped = True;

    return charge;

def main():
    items = int(input("Please enter number of items: "));
    print("{:.2f}".format(ShippingCharge(items)));

if __name__ == '__main__':
    main();
