#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program calculate the total cost of pizza

import constants


def main():
    # This function calculate the total cost of pizza

    # input
    diameter = int(input("Enter diameter of the pizza you would like(inch): "))

    # process
    sub_total = constants.LABOR + constants.RENT + (diameter * constants.COST_PER_INCH)
    total = sub_total * constants.HST

    # output
    print("")
    print("The cost for a {0} inch pizza is ${1:,.2f}".format(diameter, total))
    print("\nDone")


if __name__ == "__main__":
    main()
