#Question 2(a)
def time_to_seconds(time):
    hrs = int(time[0:2])
    mins = int(time[3:5])
    sec = int(time[6:8])

    seconds = (hrs* 3600) + (mins*60) + sec
    return seconds

time_to_seconds('01:00:25')

#Question 2(b)
def time_to_seconds(time):
    mins = int(time[0:2])
    sec = int(time[3:5])
    
    seconds = (mins*60) + sec
    return seconds

time_to_seconds('01:25')

#Question 2(c)
def time_to_seconds(time):
    if len(time) == 8 and time[2] == ':' and time[5] == ':':
        hrs = int(time[0:2])
        mins = int(time[3:5])
        sec = int(time[6:8]) 

        seconds = (hrs* 3600) + (mins*60) + sec
    
    elif  len(time) == 5 and time[2] == ':':
        mins = int(time[0:2])
        sec = int(time[3:5])
    
        seconds = (mins*60) + sec
    else:
        return None
    
    return seconds