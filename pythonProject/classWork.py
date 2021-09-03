#amber evans
#problem 10

#running problem

start_time=(6*3600)+52*60
easy_pace_miles_sec=2*(8*60+15)
temp_pace_miles_sec=3*(7*60+12)
print(start_time,easy_pace_miles_sec,temp_pace_miles_sec)
final_seconds=start_time+easy_pace_miles_sec+temp_pace_miles_sec

print(final_seconds)

finish_hours=final_seconds//60
remaining_mins=final_seconds%60

finish_mins=int(remaining_mins)
finish_seconds=(remaining_mins-int(remaining_mins))*60

print (finish_hours,finish_mins, finish_seconds)