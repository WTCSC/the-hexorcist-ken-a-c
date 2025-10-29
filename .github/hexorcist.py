# Part 1: Convert from any base to decimal
def to_decimal(number_string, original_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_string = number_string.upper()
    total_value = 0
    power = 0
    
    for char in number_string[::-1]:
        char_value = digits.index(char)  
        total_value += char_value * (original_base ** power)
        power += 1
    
    return total_value

# Part 2: Convert from decimal to any target base
def from_decimal(decimal_number, target_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if decimal_number == 0:
        return "0"
    
    result_string = ""
    number = decimal_number
    
    while number > 0:
        remainder = number % target_base
        number = number // target_base
        char_to_add = digits[remainder]
        result_string = char_to_add + result_string  # Prepend the character
    
    return result_string

# Main Program (UI)
print("Welcome to The Hexorcist! THE POWER OF MATH COMPELS YOU!")

number_string = input("Enter the number you want to convert: ")
original_base = int(input("Enter the number's CURRENT base (2-36): "))
target_base = int(input("Enter the NEW base you want (2-36): "))

decimal_value = to_decimal(number_string, original_base)

converted_value = from_decimal(decimal_value, target_base)

print(f"{number_string} (Base-{original_base}) is {converted_value} (Base-{target_base})")
