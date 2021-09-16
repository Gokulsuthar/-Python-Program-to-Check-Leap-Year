year = int(input("Year: "))

def is_leap(year: int):
    if (year % 4) == 0:
        print("{0} is a leap year".format(year))
    elif (year % 100) == 0:
        print("{0} is a leap year".format(year))
    elif (year % 400) == 0:
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))

is_leap(year)