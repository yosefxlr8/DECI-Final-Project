def read_from_file(fname) -> str:
    with open(fname, 'r') as fhandler:
        plain_text = fhandler.read()
    return plain_text
    
def write_to_file(data, fname) -> None:
    with open(fname, 'w') as fhandler:
        fhandler.write(data)
    return
