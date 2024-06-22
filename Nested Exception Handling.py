#Write a function that attempts to open a file and parse its contents as JSON. Handle exceptions for file not found, JSON decode errors, and any other unforeseen exceptions.

import json

def parse_json_file(filename):
    try:
        with open(filename, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return "Error: Failed to decode JSON."
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"
