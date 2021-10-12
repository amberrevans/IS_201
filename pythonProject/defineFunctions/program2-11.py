#Amber Evans
#Homework_1 directory
#Program 2-11

#This program collects input from the user and calculates how much money
#needs to be deposited to reach a savings goal.

def savingsGoal ():
       futureValue= float (input('Enter the desired future value: '))
       rate = float (input('Enter the annual interest rate: '))
       years = int (input('How many years will you let the money grow? '))

       presentValue = futureValue/(1+rate)**years

       print ('You will need to deposit $','{:.2f}'.format(presentValue))
       return
savingsGoal()
