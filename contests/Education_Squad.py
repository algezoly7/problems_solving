arr = []
solo = 0
duo = 0

arr = []

for _ in range(3):
    arr.append(input())

##Rows
for i in range(3):
    count = set()
    for j in range(3):
        count.add(arr[i][j])
    
    if(len(count) == 1 and count not in arr):
        arr.append(count)
        solo += 1

    elif(len(count) == 2 and count not in arr):
        arr.append(count)
        duo += 1

#Coloumns
for i in range(3):
    count = set()
    for j in range(3):
        count.add(arr[j][i])
    
    if(len(count) == 1 and count not in arr):
        arr.append(count)
        solo += 1

    elif(len(count) == 2 and count not in arr):
        arr.append(count)
        duo += 1


# Main Diagonal 
main_diagonal = [[0, 0], [1, 1], [2, 2]]
count = set()
for i in main_diagonal:
    count.add(arr[i[0]][i[1]])

if(len(count) == 1 and count not in arr):
    arr.append(count)
    solo += 1

elif(len(count) == 2 and count not in arr):
    arr.append(count)
    duo += 1

# Other Diagonal
main_diagonal = [[0, 2], [1, 1], [2, 0]]
count = set()
for i in main_diagonal:
    count.add(arr[i[0]][i[1]])

if(len(count) == 1 and count not in arr):
    arr.append(count)
    solo += 1

elif(len(count) == 2 and count not in arr):
    arr.append(count)
    duo += 1

print(solo)
print(duo)

