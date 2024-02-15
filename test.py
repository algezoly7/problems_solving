func = lambda x: x%2
x = filter(func, [1, 2, 3, 4])
for i in x:
    print(i)