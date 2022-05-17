# python3
def Extending_stack_interface():
    q = int(input())
    answer = []
    for _ in range(q):
        arr = list(map(str, input().split()))
        if(arr[0] == 'push'):
            answer.append(int(arr[1]))
        elif(arr[0] == 'max'):
            print(max(answer))
        elif(arr[0] == 'pop'):
            answer.pop()
Extending_stack_interface()