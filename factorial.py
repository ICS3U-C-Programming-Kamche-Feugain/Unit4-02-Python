#!/usr/bin/env python3\
# Created By:Kamche
# Created on: November 9, 2026
# This program asks the user for numbers
# to make during a do-while loop program
# make the users number false.


def main():
    # initializing what variables are
    loop_counter = 0
    factorial_answer = 1

    # get the user number
    while True:
        try:
            user_num_str = input("Enter a positive whole number: ")
            user_num_int = int(user_num_str)

            if user_num_int < 0:
                print(
                    "{} is a invalid entry. Please enter a positive whole number.".format(
                        user_num_str
                    )
                )
            else:
                break

        except ValueError:
            print(
                "{} is an invalid entry. Please enter a valid integer.".format(
                    user_num_str
                )
            )

    print("")

    # replicates a do..while loop
    # calculate the factorial of the user number using a loop
    while True:
        loop_counter = loop_counter + 1
        factorial_answer = factorial_answer * loop_counter

        print("Tracking {} times through loop.".format(loop_counter))

        if loop_counter >= user_num_int:
            break

    print("")
    print("{}! = {}".format(user_num_int, factorial_answer))


if __name__ == "__main__":
    main()
