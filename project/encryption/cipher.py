import string

class Cipher:
    ALPHA = string.ascii_lowercase

    def __init__(self, key) -> None:
        self.__key = key

    def encode(self, plain_text) -> str:
        key = self.__key
        cipher_text = ''
        for c in plain_text:
            tmp = c.lower()
            if tmp not in Cipher.ALPHA:
                cipher_text += c
                continue
            cap = c.isupper()
            position = Cipher.ALPHA.index(tmp)
            new_position = (position + key) % len(Cipher.ALPHA)
            new_char = Cipher.ALPHA[new_position]
            if cap: new_char = new_char.upper()
            cipher_text += new_char
        return cipher_text

    def decode(self, cipher_text) -> str:
        key = -self.__key
        return Cipher(key).encode(cipher_text)

def main() -> None:
    plain_text = input()
    key = int(input())

    encoder = Cipher(key)
    cipher_text = encoder.encode(plain_text)

    print(encoder.decode(cipher_text))


if __name__ == "__main__":
    main()