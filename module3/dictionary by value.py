dictionary = {
    'apple': 3,
    'banana': 1,
    'cherry': 2,
    'date': 4
}

sorted_dict_asc = dict(sorted(dictionary.items(), key=lambda item: item[1]))

sorted_dict_desc = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:")
print(sorted_dict_asc)

print("\nDescending order:")
print(sorted_dict_desc)

