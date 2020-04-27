#for more informations copy this link: https://www.hackerrank.com/challenges/day-of-the-programmer/problem

def dayOfProgrammer(year):
    if(year == 1918):
        year = str(year)
        return("26.09." +year)

    elif(year < 1917 and year % 4 == 0 or year > 1918 and year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
        year = str(year)
        return("12.09." +year)
    
    else:
        year = str(year)
        return("13.09." +year)

if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)
    
    print(result)