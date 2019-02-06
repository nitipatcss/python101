# def inc_vat(price):
#     return price + (price*7 / 100)
#
# def exc_vat(price):
#     return price - (price * 7 / 100)
#
# if __name__ == '__main__':
#     price = 100
#     print("Prcie with VAT will be " + str(inc_vat(price)))
#     print("Prcie without VAT will be " + str(exc_vat(price)))

import sys


def check_temp(temp):
    if temp < 15:
        return ("It's so cool")
    elif temp < 25:
        return ("It good weather")
    elif temp < 30:
        return ("It warm")
    elif temp < 40:
        return ("It so hot")
    else:
        return ("shit, It fucking hot")


if __name__ == '__main__':
    temp = input("enter your temperature: ")
    while temp != 'q':

        if temp.isnumeric():
            temp = int(temp)
            print(check_temp(temp))
        else:
            print("You must enter mumber or 'q' only.")

        temp = int(input("enter your temp again.. :"))

    sys.exit(0)
