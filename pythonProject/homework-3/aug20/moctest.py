#mock test question
#if I got home at 7:30:06 after running 3 miles at a pace of 7:15 and 2 miles at 6:18 what time did
#i start?

pace1 = ((7*60)+15)*3
pace2 = ((6*60)+18)*2

hoursTosec = (7*3600)
minsTosec = (30*60)
totalTimesec = (hoursTosec+ minsTosec+6)

returnTimeinSec = (totalTimesec-pace1-pace2)
returntimeinHours = returnTimeinSec//3600
remainingSeconds = returnTimeinSec%3600

returntimeinmins = remainingSeconds//60
returntimeinseconds = returnTimeinSec%60

print('The time you left was',returntimeinHours,':' ,returntimeinmins,':',returntimeinseconds)