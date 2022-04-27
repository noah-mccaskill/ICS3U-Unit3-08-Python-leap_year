# /usr/bin/env python3

# Created by: Noah McCaskill
# Created on: April 2022
# This program asks for the user's year to determine if it is a leap year


def main():
    # this function checks if the user's chosen year is a leap or common year

    # input
    year = input("Enter a year: ")
    print("")

    # process & output
    try:
        integer_as_number = int(year)

        if integer_as_number % 4 == 0:

            if integer_as_number % 100 == 0:

                if integer_as_number % 400 == 0:
                    print("It is a leap year.")

                else:
                    print("It is a common year.")

            else:
                print("It is a leap year.")

        else:
            print("It is a common year.")

    except Exception:
        print("That is not a year.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
