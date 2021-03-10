from morse import morse_dict


def convert_string(string):
    morse_code = ''
    for char in string:
        try:
            if char == ' ':
                morse_code += '       '
            else:
                morse_code += morse_dict[char.lower()]
                morse_code += '   '
        except KeyError:
            print("\nOne of your characters is not recognized by the program. Please try again.")
            string_to_convert = input("\nType some text to convert: ")
            convert_string(string_to_convert)
    return morse_code


def morse_converter():
    print("Alex's Morse Code Converter")
    while True:
        string_to_convert = input("\nType some text to convert: ")
        print(convert_string(string_to_convert))
        convert_again = input("\nWould you like to convert more text to Morse code? Type 'y' or 'n': ").lower()
        if convert_again != 'y':
            print("\nGoodbye!")
            break


morse_converter()

# TODO: take in a string to be converted
# TODO: perform a type-check on the input string
# TODO: iterate through the string and convert letters/numbers into Morse
# TODO: handle spaces between letters and words
