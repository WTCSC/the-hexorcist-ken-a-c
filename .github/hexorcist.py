def to_decimal(number_string, original_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_string = number_string.upper()
    total = 0
    power = 0
    i = len(number_string) - 1

    while i >= 0:
        char = number_string[i]

      for index in range(len(digits)):
            if digits[index] == char:
                value = index
                break
        total = total + value * (original_base ** power)
        power = power + 1
        i = i - 1
    
    return total

def from_decimal(decimal_number, target_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if decimal_number == 0:
        return "0"
    
    result = ""
    number = decimal_number
    while number > 0:
        remainder = number % target_base
        number = number // target_base
        result = digits[remainder] + result 
    
    return result

print("Welcome to The Hexorcist! THE POWER OF MATH COMPELS YOU!")

number_string = input("Enter the number you want to convert: ")
original_base = int(input("Enter the number's CURRENT base (2-36): "))
target_base = int(input("Enter the NEW base you want (2-36): "))

decimal_value = to_decimal(number_string, original_base)
converted_value = from_decimal(decimal_value, target_base)

print(number_string + " (Base-" + str(original_base) + ") is " + converted_value + " (Base-" + str(target_base) + ")")

