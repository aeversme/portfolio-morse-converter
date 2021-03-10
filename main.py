from morse import morse_dict


def convert_string(string):
    morse_code = ''
    for char in string:
        if char == ' ':
            morse_code += '       '
        else:
            morse_code += morse_dict[char.lower()]
            morse_code += '   '
    return morse_code


def morse_converter():
    print("Alex's Morse Code Converter")
    while True:
        string_to_convert = input("\nType some text to convert: ")
        try:
            print(convert_string(string_to_convert))
        except KeyError:
            print("\nOne of the entered characters is not recognized by the program. Please try again.")
        else:
            convert_again = input("\nWould you like to convert more text to Morse code? Type 'y' or 'n': ").lower()
            if convert_again != 'y':
                print("\nGoodbye!")
                break


morse_converter()
