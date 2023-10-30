from collections import Counter

data = [{'item': 'item1', 'amount': 400},
        {'item': 'item2', 'amount': 300},
        {'item': 'item1', 'amount': 750}]

# Create a Counter object to aggregate the values
result = Counter()

for item_dict in data:
    item_name = item_dict['item']
    amount = item_dict['amount']
    result[item_name] += amount

# Convert the result Counter to a regular dictionary
result_dict = dict(result)

print(result_dict)
