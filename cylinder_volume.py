#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Jan 2021
# This program for return_values


import math


def cylinder_volume(radius, height):
    # This function is for calculate the vilume of the cylinder

    # process
    try:
        radius_int = int(radius)
        if radius_int > 0:
            try:
                height_int = int(height)
                if height_int > 0:
                    volume = radius_int ** 2 * math.pi * height_int

                    return volume
                else:
                    print("The height is not a positive number")
            except Exception:
                print("The height is not a integer")
        else:
            print("The radius is not a positive number")
    except Exception:
        print("The radius is not a integer")


def main():
    # This function is get input

    # input

    radius = input("Enter the radius(mm):")
    height = input("Enter the height(mm):")

    # call function
    volume = cylinder_volume(radius, height)

    # output
    print("The volume of the cylinder is: {0}mm³".format(volume))


if __name__ == "__main__":
    main()
