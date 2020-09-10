#for more informations copy this link: https://www.hackerrank.com/challenges/library-fine/problem

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 < y2 or (m1 < m2 and y1 == y2) or (d1 <= d2 and m1 == m2 and y1 == y2):
        return(0)
    elif(d1 > d2 and m1 == m2 and y1 == y2):
        number_of_days_late = d1 - d2
        return(number_of_days_late * 15)
    elif(m1 > m2 and y1 == y2):
        number_of_months_late = m1 - m2
        return(number_of_months_late * 500)
    elif(y1 > y2):
        number_of_years_late = 10000
        return(number_of_years_late)
        
if __name__ == '__main__':

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    print(result)
