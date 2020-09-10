#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/which-day/problem

import datetime 
import calendar 

def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born]) 

# Driver program 
t = int(input())
for _ in range(t):
    date = input()
    print(findDay(date).upper()) 