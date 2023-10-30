from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Create Counter objects from the dictionaries
counter1 = Counter(d1)
counter2 = Counter(d2)

# Add the two Counter objects
result_counter = counter1 + counter2

# Convert the result Counter to a regular dictionary
result_dict = dict(result_counter)

print(result_dict)
