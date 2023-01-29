import file_handler
import sha256_hashing

def generate(fname1, fname2=None):
    plain_text = file_handler.read_from_file(fname1)
    hash_value = sha256_hashing.hash(plain_text)
    if fname2:
        file_handler.write_to_file(hash_value, fname2)
    return hash_value

def compare(fname1, fname2):
    hash_value = generate(fname1)
    registered = file_handler.read_from_file(fname2)

    return hash_value == registered

def main():
    mode = int(input("Mode(Generate:1, Compare:2):"))
    fname1, fname2 = input().split()

    integrity = (generate, compare)[mode-1](fname1, fname2)
    print(("Integrity-Violated","Integrity-Confirmed")[integrity])


if __name__ == "__main__":
    main()

    