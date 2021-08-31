#Amber Evans
#IS 210-01

#Homework_1
#Program 2-13

#This program illustrates the issues caused by uninitalized variables
#the variavle test3 is never initialized, so it will cause an error
#To fix this issue, a test3 variable needs to initialized

#Declare variables and initialize to float values
test1 = 88.0
test2 = 92.5

#Calculate average as float since formula incluses float variables
average = (test1+ test2+test3)/3

#output the value of average with automatic space between
print ("Your average score is", average)
