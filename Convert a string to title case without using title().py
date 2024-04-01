#Write a python program to convert a string to title case without using the title().

string = input("Enter a string: ")

def to_title_case(s):
    return ' '.join(word.capitalize() for word in s.split())

title_case_string = to_title_case(string)

print("Title case string:", title_case_string)
