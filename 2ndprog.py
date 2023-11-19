def and_xor_operations(input_string):
    and_result = ""
    xor_result = ""

    for char in input_string:
        # Get the Unicode code point of the character
        code_point = ord(char)

        # AND each code point with 127
        and_result += chr(code_point & 127)

        # XOR each code point with 127
        xor_result += chr(code_point ^ 127)

    return and_result, xor_result

# The input string
input_string = "Hello World"

# Perform AND and XOR operations on each character with 127
and_result, xor_result = and_xor_operations(input_string)

# Display the results
print(f"Original String: {input_string}")
print(f"AND Result: {and_result}")
print(f"XOR Result: {xor_result}")