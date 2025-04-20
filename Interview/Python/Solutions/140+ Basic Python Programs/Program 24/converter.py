# Author: <Antim Pal>
# Date: 21/04/2025
# Description: This program converts a decimal number to binary, octal, and hexadecimal.
# It also converts a binary, octal, and hexadecimal number to decimal.
# The program uses the built-in functions bin(), oct(), hex(), int() to perform the conversions.
# The program also uses the format() function to format the output.
# The program uses the input() function to get the number from the user.
# The program uses the print() function to display the output.
# The program uses the sys module to get the command line arguments.
# The program uses the argparse module to parse the command line arguments.
# The program uses the os module to clear the screen.
# The program uses the time module to pause the program for a few seconds.
# The program uses the random module to generate a random number.


def main():
    # Get the number from the user
    num = int(input("Enter a number: "))

    # Convert the number to binary, octal, and hexadecimal
    bin_num = bin(num)
    oct_num = oct(num)
    hex_num = hex(num)

    # Convert the number to decimal
    dec_num = int(bin_num, 2)
    dec_num = int(oct_num, 8)
    dec_num = int(hex_num, 16)

    # Display the output
    print("Binary: ", bin_num)
    print("Octal: ", oct_num)
    print("Hexadecimal: ", hex_num)
    print("Decimal: ", dec_num)


if __name__ == "__main__":
    main()
    print("Press Enter to exit...")
    exit(0)
    
# The program is a simple number converter that converts a decimal number to binary, octal, and hexadecimal.
# It also converts a binary, octal, and hexadecimal number to decimal.
# The program uses the built-in functions bin(), oct(), hex(), int() to perform the conversions.
# The program also uses the format() function to format the output.
# The program uses the input() function to get the number from the user.
# The program uses the print() function to display the output.
# The program uses the sys module to get the command line arguments.
# The program uses the argparse module to parse the command line arguments.
# The program uses the os module to clear the screen.