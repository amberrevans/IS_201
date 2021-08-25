#convert user input to Integer and store in hits
hits = int(input('Enter the players number of hits: '))

#Convert user input to Integer and store in atBat
atBat = int(input('Enter the players number of times at bat: '))

#Calculate the batting average
battingAverage = hits/atBat

#Display the batting average with default spacing
print ("The player's batting average is ", battingAverage)
