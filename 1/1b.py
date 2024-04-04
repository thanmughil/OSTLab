decimal_input = int(input("Enter a decimal number: "))

binary_number = bin(decimal_input)
octal_number = oct(decimal_input)
hexadecimal_number = hex(decimal_input)

print(f"Decimal: {decimal_input}")
print(f"Binary: {binary_number}")
print(f"Octal: {octal_number}")
print(f"Hexadecimal: {hexadecimal_number}")