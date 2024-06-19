#Write a function that reads a file and returns its content. If the file does not exist, raise an exception.

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("The specified file does not exist.")
