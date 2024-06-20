#Write a function that opens a file, writes some data to it, and ensures the file is always closed properly using the finally block.

def write_to_file(filename, data):
    try:
        file = open(filename, 'w')
        file.write(data)
    except Exception as e:
        return f"Error: {e}"
    finally:
        file.close()
