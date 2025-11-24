#Question 1(a)
def seconds_to_time(time):
    time_in_seconds = int(time)

    if time_in_seconds >= 60:               #convert to mins and secs if time 
        sec = time_in_seconds % 60
        min = time_in_seconds // 60
        if min >= 60:                       #convert to hours
            hrs = min // 60
            min = min % 60
            new_time = str('%02d' % hrs) + ':' + str('%02d' % min) + ':' + str('%02d' % sec)
        else:
            hrs = 0
            new_time = str('%02d' % hrs) + ':' + str('%02d' % min) + ':' + str('%02d' % sec)       #if not upto an hour, set hours to zero and print time
    else:
        min = 0
        hrs = 0 
        new_time = str('%02d' % hrs) + ':' + str('%02d' % min) + ':' + str('%02d' % time_in_seconds)  #if not upto a minute, set hours and mins to zero and print time
    return new_time

seconds_to_time(3625)

#Question 1(b)
def seconds_to_time(time):
    time_in_seconds = int(time)

    if time_in_seconds >= 60:   
        sec = time_in_seconds % 60
        min = time_in_seconds // 60
        if min >= 60:
            hrs = min // 60
            min = min % 60
            new_time = str('%02d' % hrs) + ':' + str('%02d' % min) + ':' + str('%02d' % sec)
        else:
            new_time = str('%02d' % min) + ':' + str('%02d' % sec)
    else:
        min = 0
        new_time = str('%02d' % min) + ':' + str('%02d' % time_in_seconds)
    return new_time
seconds_to_time(85)
seconds_to_time(16)

#Question 1(c)
def seconds_to_time(time):
    time_in_seconds = int(time)
    if time_in_seconds < 0 or time_in_seconds > 359999:   # 99:59:59 in seconds
        return None
    
    elif time_in_seconds >= 60:   
        sec = time_in_seconds % 60
        min = time_in_seconds // 60
        if min >= 60:
            hrs = min // 60
            min = min % 60
            new_time = str('%02d' % hrs) + ':' + str('%02d' % min) + ':' + str('%02d' % sec)
        else:
            new_time = str('%02d' % min) + ':' + str('%02d' % sec)
    else:
        min = 0
        new_time = str('%02d' % min) + ':' + str('%02d' % time_in_seconds)
    return new_time
seconds_to_time(-12)