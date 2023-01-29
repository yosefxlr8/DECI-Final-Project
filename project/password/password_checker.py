import Password

def main():
    test = input("Password: ")
    password = Password.Password(test)
    password.categorise()
    print()
    print(password.strength)
    print()
    new_password = Password.Password.PasswordGenerator().gen_password()
    print(f"Suggestion: {new_password}")

if __name__ == "__main__":
    main()
