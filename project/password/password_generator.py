import sys

import Password 

def main(arguments):
    generator = Password.Password.PasswordGenerator(*arguments)

    passwords = []
    for _ in range(passwords_no):
        password = generator.gen_password()
        passwords.append(password)
        print(password)
    
    return passwords

if __name__ == "__main__":
    if len(sys.argv) > 1:
        passwords_no, *arguments = sys.argv
        arguments = map(int, arguments)
    else:
        passwords_no = int(input("Number of passwords:"))

        standard = int(input("Standard(True 1, False:0): "))
        if standard:
            arguments=[]
        else:
            length = int(input("Password length(int):"))
            caps = int(input("Capital letters(True:1, False:0):"))
            digits = int(input("Digits(True:1, False:0):"))
            specials = int(input("special characters(True:1, False:0):"))

            arguments = [length, caps, digits, specials]
    print("\nPasswords:")
    main(arguments)

# code by: Youssef Mahmoud Abdelwahed