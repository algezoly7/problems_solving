from collections import defaultdict

n = int(input())
dictionary = defaultdict(int)
for _ in range(n):
    x, y = map(str, input().split())
    dictionary[x] = y

while(True):
    try:
        x = input()
    except EOFError:
        break

    if(dictionary[x] != 0):
        print(x + "=" + dictionary[x])
    else:
        print("Not found")