#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: Oct 2022
# This program display a month based on your input
# NOTE: This will only work on >= Python 3.10


def main():
    # this function checks checks what month a user chooses

    # input the integer representing a month
    user_month = input("Enter a month as an integer(ex: 1 is January): ")
    print("")

    # process & output
    # process - assign each integer to a month
    # output the integer they inputted along with its corresponding month
    match user_month:
        case "1":
            print("1 is January!")
        case "2":
            print("2 is February")
        case "3":
            print("3 is March")
        case "4":
            print("4 is April")
        case "5":
            print("5 is May")
        case "6":
            print("6 is June")
        case "7":
            print("7 is July")
        case "8":
            print("8 is August")
        case "9":
            print("9 is September")
        case "10":
            print("10 is October")
        case "11":
            print("11 is November")
        case "12":
            print("12 is December")
        case _:
            print("Error, invalid month.")


if __name__ == "__main__":
    main()
