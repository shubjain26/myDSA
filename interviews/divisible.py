"""
Problem Statement: Given a fractional number
find whether it results into a non repeating number

Company: Bosch
Date: 11-Oct-2022

Approach:
    Check if numerator is completely divisible by denominator
    if not, divide it by max possible multiple and remainder is new numerator
    keep storing the remainder, if the remainder repeats then it is not completely divisible
    multiply numerator by 10 if numerator is less than denominator

Difficulty: Easy
Topic: Hash map
"""


def divisible_check(num, den):

    onum = num
    res = True
    quotient = "0"
    first_zero = True
    if den == 0:
        return False
    elif num % den == 0:
        return True
    else:
        rem = num
        remainders = {}
        while rem > 0:

            if num < den:
                num = num * 10
                if first_zero:
                    quotient += "."
                    first_zero = False

            quotient += str(num // den)

            rem = num % den
            num = rem

            if not rem in remainders:
                remainders[rem] = 1
            else:
                res = False
                break

    print(f"number: {onum}/{den}, quotient: {float(quotient)}, divisible: {res}")
    return res


divisible_check(1, 2)
divisible_check(4, 3)
divisible_check(10, 2)
divisible_check(1, 3)
divisible_check(22, 7)
