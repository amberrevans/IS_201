#Amber Evans
#IS2310-01

#Homework_1 directory
#Program 2-11

#This program collects input from the user and calculates how much money
#needs to be deposited to reach a savings goal.

#Convert user input to float and store in futureValue
futureValue = float(input("Enter the desired future value: "))

#Convert user input to float and store in rate
rate = float(input("Enter the annual interest rate: "))

#convert user input to integer and store in years
years = int(input("How many years will you let the money grow? "))

#calculate present value and store in presentValue
#Python uses the ** symbol when raising a number to a power
presentValue=futureValue/(1+rate)**years

#display with formatted float value and no automatic space
print ("You will need to deposit $",\
       format (presentValue, ",.2f"),\
       sep="")
