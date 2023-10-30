def is_number_in_range(number, lower_limit, upper_limit):
    if lower_limit <= number <= upper_limit:
        return True
    else:
        return False

# Example usage:
number = 44
lower_limit = 10
upper_limit = 50

if is_number_in_range(number, lower_limit, upper_limit):
    print(f"{number} is in the range [{lower_limit}, {upper_limit}]")
else:
    print(f"{number} is not in the range [{lower_limit}, {upper_limit}]")
