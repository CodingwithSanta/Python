def str_val(input_string):
    hash_upper = any(c.isupper() for c in input_string)
    hash_lower = any(c.islower() for c in input_string)
    hash_digit = any(c.isdigit() for c in input_string)

    return hash_upper and hash_lower and hash_digit
input_string = "Passcode"
print("string validation",str_val(input_string))
