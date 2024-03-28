#Count the number of vowels in a string provided by the user.

string = input("Enter a string: ")
vowels = "aeiouAEIOU"

vowel_count = sum(1 for char in string if char in vowels)

print("Number of vowels in the string:", vowel_count)
