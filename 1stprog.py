def xor_with_zero(input_string):
    result = ""
    for char in input_string:
        # Get the Unicode code point of the character and XOR it with 0
        xor_result = ord(char) ^ 0
        # Convert the result back to a character and append to the output string
        result += chr(xor_result)
    return result

# The input string
input_string = "Hello World"

# XOR each character with 0
result_string = xor_with_zero(input_string)

# Display the result
print(f"Original String: {input_string}")
print(f"XOR Result: {result_string}")