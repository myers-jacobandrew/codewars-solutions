def two_decimal_places(number):
    return float(str(number)[:str(number).index('.') + 3])