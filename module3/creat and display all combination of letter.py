from itertools import product

data = {'1': ['a', 'b'], '2': ['c', 'd']}


combinations = [''.join(i) for i in product(*data.values())]


for i in combinations:
    print(i, end=' ')


print()
