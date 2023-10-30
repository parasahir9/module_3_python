sample_string = 'w3resource'

# Initialize an empty dictionary to store the letter counts
letter_count = {}

# Iterate through the characters in the string
for char in sample_string:
    # Check if the character is a letter (ignore digits)
    if char.isalpha():
        # Convert the character to lowercase for case-insensitive counting
        char = char.lower()
        # Update the letter count in the dictionary
        letter_count[char] = letter_count.get(char, 0) + 1

# Print the resulting letter count dictionary
print(letter_count)
