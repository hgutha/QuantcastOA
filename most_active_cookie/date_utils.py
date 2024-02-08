def is_valid_date_format(date):
    date_arr = date.split('-')
    # Check if date has 3 components for year, month, and day
    if len(date_arr) != 3:
        return False
    year, month, day = date_arr
    # Check if the 3 components represent numbers
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    # Check if YYYYMMDD format
    if not (len(year) == 4 and len(month) == 2 and len(day) == 2):
        return False
    # Check if MM is valid and DD is valid
    if not (0 < int(month) <= 12 and 0 < int(day) <= 31):
        return False
    # Check February and leap year edge cases
    if int(month) == 2:
        if int(year) % 4 == 0:
            if int(day) > 29:
                return False
        else:
            if int(day) > 28:
                return False
    return True


def date_to_string(date):
    formatted_date = date.split('T')[0]
    # Check validity of date format
    if not is_valid_date_format(formatted_date):
        raise ValueError("Invalid date or date is not in YYYY-MM-DD format.")

    # Split the date into YYYY, MM, DD
    date_arr = formatted_date.split('-')
    # Create "YYYYMMDD" string from date_arr
    date_string = str(date_arr[0]).strip() + str(date_arr[1]).strip() + str(date_arr[2]).strip()
    return date_string
