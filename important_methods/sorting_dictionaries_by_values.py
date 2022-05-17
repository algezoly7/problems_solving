#sorting dictionaries by values example.
purse = {}
purse['c'] = 0
purse['b'] = 5
purse['a'] = purse.get(3, 0) + 1
list_ = []
for key, value in purse.items():
    #we flip the keys and the values .
    list_.append((value, key))
list_ = sorted(list_)
print(list_)



#read about list comprehension