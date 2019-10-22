from Basic_data_structures import stack


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"

    rem_stack = stack.Stack()

    while dec_number > 0:
        rem = dec_number % base
        print("Rem: ", rem)
        rem_stack.push(rem)
        dec_number = dec_number // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]
        print("Digits: ", new_string)
    return new_string


print(base_converter(25, 2))
print("*****************")
print(base_converter(25, 8))
print("*****************")
print(base_converter(25, 16))
