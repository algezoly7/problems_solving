#for more informations copy this link: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

def catAndMouse(x, y, z):
    catA_distance = abs(x - z)
    catB_distance = abs(y - z)
    if(catA_distance < catB_distance):
        return("Cat A")

    elif(catB_distance < catA_distance):
        return("Cat B")

    else:
        return("Mouse C")
        
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)
