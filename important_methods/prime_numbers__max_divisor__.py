#for more informations copy this link: https://youtu.be/2p3kwF04xcA.
#to find out whether a number is a prime one.
import math
n = int(input())
max_divisor = math.ceil(math.sqrt(n))
tracker = True
#all prime numbers are odd numbers.
if(n != 2 and n % 2 == 0):
    tracker = False
#odd numbers can't have even numbers as coefficients.
else:
    for i in range(3, max_divisor + 1, 2):
        if(n % i == 0):
            tracker = False
            break
print(tracker)
