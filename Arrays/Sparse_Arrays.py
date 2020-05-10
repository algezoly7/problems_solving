#for more informations copy this link: https://www.hackerrank.com/challenges/sparse-arrays/problem

n = int(input())
strings= []
for _ in range(n):
    string = input()
    strings.append(string)
q = int(input())
queries = []

for _ in range(q):
    query = input()
    queries.append(query)

def matchingStrings(strings_array, queries_arry):
    for i in range(q):
        counter = 0
        for num in range(n):
            if(queries_arry[i] == strings_array[num]):
                counter += 1
        print(counter)

matchingStrings(strings, queries)