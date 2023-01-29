import cipher
import file_handler

def main() -> None:
    mode = int(input("Mode(encrypt: 1, decrypt: 2): "))
    fname1 = input("File path: ")
    fname2 = input("New file path: ")
    key = int(input("Encryption key(the shifting value): "))

    encoder = cipher.Cipher(key)
    plain_text = file_handler.read_from_file(fname1)
    cipher_text = (encoder.encode, encoder.decode)[mode-1](plain_text)

    file_handler.write_to_file(cipher_text, fname2)
    print('Done')
    
if __name__ == "__main__":
    main()