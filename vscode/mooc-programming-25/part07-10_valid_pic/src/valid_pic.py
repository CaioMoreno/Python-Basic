from datetime import *


def is_it_valid(pic: str) -> bool:
    s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'A', 'B', 'C', 'D', 'E', 'F', 'H', 'J', 'K', 'L',
         'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

    if len(pic) != 11:
        return False

    # Determine century
    if pic[6] == '+':
        cent = 1800
    elif pic[6] == '-':
        cent = 1900
    elif pic[6] == 'A':
        cent = 2000
    else:
        return False

    # Extract and validate date components
    try:
        day = int(pic[0:2])
        month = int(pic[2:4])
        year = int(pic[4:6]) + cent
        ident = int(pic[7:10])
    except ValueError:
        return False

    # Validate date ranges
    if not (1 <= day <= 31 and 1 <= month <= 12):
        return False

    # Validate days for specific months
    if month == 2:
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            if day > 29:
                return False
        elif day > 28:
            return False
    elif month in {4, 6, 9, 11} and day > 30:
        return False

    # Calculate the control character
    control_number = int(f"{pic[0:6]}{pic[7:10]}") % 31
    if pic[10] != s[control_number]:
        return False

    return True
