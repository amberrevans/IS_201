#convert seconds to days, hours, minutes, seconds

seconds = float(input('Please enter a number of seconds: '))

def conv_time ():
    #number of days in the seconds
    days = seconds / 86400
    daysR = seconds % 86400

    #number of hours remaining
    hours = days / 3600
    hoursR = days % 3600

    #number of minutes remaining
    minutes = hours / 60
    minutesR = hoursR %60


    print ("Hours: ","{:.2f}".format(hours))
    print ('Days:',"{:.2f}".format(days))
    print ('Minutes: ','{:.2f}'.format(minutesR))

    return
conv_time()

