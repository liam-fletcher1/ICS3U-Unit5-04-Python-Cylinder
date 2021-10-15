#!/usr/bin/env python3

# Created by : Liam Fletcher
# Created on : October 2021
# This program uses the radius and height to
# find the volume of a cylinder

import math


def volume_cy(radius, height):
    # calculates the volume of cylinder

    volume = round(math.pi * pow(radius, 2), 2) * height

    return volume


def main():
    # This program uses the radius and height to
    # find the volume of a cylinder

    # input
    radius_user = input("Enter the radius for the cylinder (mm): ")
    height_user = input("Enter the height for the cylinder (mm): ")

    # call function
    try:
        radius_user_int = int(radius_user)
        height_user_int = int(height_user)
        calculated_volume = volume_cy(radius=radius_user_int, height=height_user_int)

        print("The volume of the cylinder is {0}mm³".format(calculated_volume))

    except Exception:
        print("")
        print("Theses are invaild numbers.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
