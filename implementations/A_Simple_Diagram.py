#for more informations copy this link : https://www.hackerrank.com/contests/easyhack2/challenges/a-simple-diagram

n = int(input())
arr = list(map(int, input().split()))
brr = [0] * 8
for i in range(n):
    if arr[i] <= 100 and arr[i] >= 95:
        brr[0] += 1
    elif arr[i] <= 94 and arr[i] >= 90:
        brr[1] += 1
    elif arr[i] <= 89 and arr[i] >= 85:
        brr[2] += 1
    elif arr[i] <= 84 and arr[i] >= 80:
        brr[3] += 1
    elif arr[i] <= 79 and arr[i] >= 70:
        brr[4] += 1
    elif arr[i] <= 69 and arr[i] >= 60:
        brr[5] += 1
    elif arr[i] <= 59 and arr[i] >= 50:
        brr[6] += 1
    elif arr[i] <= 49:
        brr[7] += 1

print('GRADE' + ' ' + '|' + ' '+ 'STUDENTS')
print('   A+' + ' ' + '|' + ' '+ '*'*brr[0])
print('   A' + '  ' + '|' + ' '+ '*'*brr[1])
print('   B+' + ' ' + '|' + ' '+ '*'*brr[2])
print('   B' + '  ' + '|' + ' '+ '*'*brr[3])
print('   C+' + ' ' + '|' + ' '+ '*'*brr[4])
print('   C' + '  ' + '|' + ' '+ '*'*brr[5])
print('   D' + '  ' + '|' + ' '+ '*'*brr[6])
print('   F' + '  ' + '|' + ' '+ '*'*brr[7])