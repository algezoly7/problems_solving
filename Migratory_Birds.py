#for more informations vist https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr):
    bird_frequency = [0, 0, 0, 0, 0, 0]

    for i in range(arr_count):
        bird_frequency[arr[i]] += 1

    return(bird_frequency.index(max(bird_frequency)))

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)