#Implement a context manager using a class that opens a file, allows reading its contents, and ensures the file is closed properly even if an exception occurs during file operations.

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"Exception: {exc_value}")
            return True

with FileManager('test.txt', 'r') as file:
    content = file.read()
    print(content)
