def count_strings(strings):
    count = 0
    for i in strings:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    return count

strings = ["abc", "aaa", "bbb", "aba", "xyz", "123", "121", "abcabc"]
print(count_strings(strings))