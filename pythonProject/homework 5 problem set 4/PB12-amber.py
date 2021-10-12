#input month number and print number of days in that month

month = int(input('Enter the month number (1-12): '))

if month < 13:
    if month ==2:
        year = int(input('year: '))
        if year %4==0:
            if year % 100 ==0:
                if year %400 == 0:
                    print ('29 days')
                else:
                    print ('28 days')
            else:
                print ('29 days')
        else:
            print ('28 days')
    elif month >= 8:
        if month %2 ==0:
            print ('31 days')
        else:
            print ('30 days')
    elif month % 2 ==0:
        print('30 days')
    else:
        print ('31 days')
else:
    print ('only 1-12 accpeted')
