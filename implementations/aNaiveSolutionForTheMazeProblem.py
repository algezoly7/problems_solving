#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/armaze

def is_safe(arr, x, y):
    if(0 <= x < m and 0 <= y < n and arr[x][y] == 1 ):
        return(True)
    
    return(False)

def solvemaze(arr, x, y, sol, d):
    if( x == x_des and y == y_des):
        sol[x][y] = 1
        return(True)
    if(is_safe(arr, x, y)):
        sol[x][y] = 1
        if(d != 'up' and solvemaze(arr, x+1, y, sol, 'down')):
            return True
        if(d != 'left' and solvemaze(arr, x, y + 1, sol, 'right')):
            return(True)
        if(d != 'down' and solvemaze(arr, x - 1, y, sol, 'up')):
            return True
        if(d != 'right' and solvemaze(arr, x, y - 1, sol, 'left')):
            return(True)
        sol[x][y] = 0
        return(False)

def solution(arr, x, y):
    sol = [[0 for j in range(n)] for i in range(m)]
    if not(solvemaze(arr, x_beg, y_beg, sol, 'up')):
        return('no')
    return('yes')

T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    maze = []
    for i in range(m):
        brr = list(input())
        maze.append(brr)

    arr = []
    for i in range(m):
        brr = [0] * n
        arr.append(brr)

    for i in range(m):
        for j in range(n):
            if(maze[i][j] == '.'):
                arr[i][j] = 1
            elif(maze[i][j] == 'X'):
                arr[i][j] = 0
            elif(maze[i][j] == 'M'):
                arr[i][j] = 1
                x_beg = i
                y_beg = j
            elif(maze[i][j] == '*'):
                arr[i][j] = 1
                x_des = i
                y_des = j
    print(solution(arr, m, n))