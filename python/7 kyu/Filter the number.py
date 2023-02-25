def filter_string(string):
    numbers = [char for char in string if char.isdigit()]
    return int(''.join(numbers))