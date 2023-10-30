def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
 
 
# Driver Code
tups = [("paras", 10), ("rina", 12), ("ahir", 14),
        ("tulsi", 20), ("wizzard", 25), ("hastar", 30)]
dictionary = {}
print(Convert(tups, dictionary))