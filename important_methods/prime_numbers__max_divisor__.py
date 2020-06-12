#for more informations copy this link: https://youtu.be/2p3kwF04xcA .
#to find out whether a number is a prime one .
import math
n = int(input())
max_divisor = math.floor(math.sqrt(n))
tracker = True
for i in range(3, max_divisor, 2):
    if(n % i == 0):
        tracker = False
print(tracker)