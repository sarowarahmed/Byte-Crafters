#Write a function that uses a context manager to open a file, process its contents, and handle exceptions gracefully while ensuring resources are cleaned up.

class FileProcessor:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
            return True

def process_file(filename):
    try:
        with FileProcessor(filename) as file:
            # Simulate processing
            content = file.read()
            print(content)
    except Exception as e:
        print(f"Failed to process file: {e}")

process_file('example.txt')
