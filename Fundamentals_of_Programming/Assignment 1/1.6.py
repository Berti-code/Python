def is_leap(year):
    if year%4==0 and year%100==0:
        return False
    elif year%4==0 and year%100!=0:
        return True

def determine_month(year,day):
    number_of_days=31
    number_of_month=1
    while day-number_of_days > 0:
        months=(4,6,9,11)
        day-=number_of_days
        number_of_month+=1
        if number_of_month == 2:
            if is_leap(year) == True:
                number_of_days=29
            else:
                number_of_days=28
        elif number_of_month in months :
            number_of_days=30
        else:
            number_of_days=31
    return (number_of_month,day)

if __name__ == '__main__':
    year=int(input("Year="))
    day=int(input("Day="))
    month,day=determine_month(year, day)
    print(day,month,year) 
    