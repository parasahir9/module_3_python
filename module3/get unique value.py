def get_unique_values(my_list):
    unique_values = []
    for value in my_list:
        if value not in unique_values:
            unique_values.append(value)
    return unique_values

# Test the function with various inputs 
my_list = [1, 2, 3, 4, 5, 2, 3, 4, 5]
print(get_unique_values(my_list))

my_list = ['apple', 'banana', 'cherry', 'banana', 'cherry']
print(get_unique_values(my_list)) 

my_list = [1, 1, 1, 1, 1]
print(get_unique_values(my_list)) 

my_list = []
print(get_unique_values(my_list)) 