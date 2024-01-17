def convert_to_int(arg):
    roman_numerals = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}
    total_num = 0
    roman_value = 0
    no_of_times = 0
    invalid = f"Invalid roman numeral '{arg}', can't convert!"
    for x in arg:
        if x not in roman_numerals.keys():
            return f"Sorry you provided a non roman numeral character, {x}.\nCheck and correct!"
        if roman_numerals[x] < 1000:
            no_of_times += 1 
        if roman_value >= roman_numerals[x]:
            if roman_value > roman_numerals[x]:
                total_num += roman_value
                no_of_times -= 1
            elif no_of_times == 0:
                total_num += roman_value
            elif no_of_times <= 3 and 2*(roman_value) not in roman_numerals.values():
                total_num += roman_value
            else:
                return invalid
            roman_value = roman_numerals[x]
        elif roman_value < roman_numerals[x]:
            if roman_value == 0:
                roman_value = roman_numerals[x]
            elif (roman_numerals[x] /  roman_value) in (5, 10) and roman_value in (100, 10, 1):
                total_num += (roman_numerals[x] - roman_value)
                roman_value = 0
                no_of_times = 0
            else: 
                return invalid
    return total_num + roman_value

def get_input():
    print(convert_to_int(input("Enter the roman numeral to be converted: ").upper()))
    if input("Would you like to continue(y/n): ").lower() == "y":
        get_input()
    else:
        print("Okay, Goodbye!")

get_input()
