decimal_input = int(input("Enter a decimal number: "))

def binCon(num):
    bin_output = ''
    while num > 0:
        bin_output = str(num % 2) + bin_output
        num = int(num / 2)
    print(bin_output if bin_output else '0')

def octCon(num):
    oct_output = ''
    while num > 0:
        oct_output = str(num % 8) + oct_output
        num = int(num / 8)
    print(oct_output if oct_output else '0')

def hexCon(num):
    hex_output = ''
    hex_chars = '0123456789ABCDEF'
    while num > 0:
        hex_output = hex_chars[num % 16] + hex_output
        num = int(num / 16)
    print(hex_output if hex_output else '0')

binCon(decimal_input)
octCon(decimal_input)
hexCon(decimal_input)
