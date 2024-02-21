n = int(input())

dictionary = {}
for _ in range(n):

    input_ = input()

    if(input_ not in dictionary):
        print("OK")
        dictionary[input_] = 0
    
    else:
        dictionary[input_] += 1
        print(input_ + str(dictionary[input_]))