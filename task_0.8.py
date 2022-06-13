
def convert(sec):
    

    hour = sec // 60
    sec %= 60 
    minutes = sec 
    if (hour==1 and minutes==1):
        print(hour, "hour", minutes, "minute")
    elif(hour==1 and minutes>1):
        print(hour, "hour", minutes, "minutes")
    elif(hour >1 and minutes ==1):
        print(hour, "hours", minutes, "minute")
    else:
        print(hour, "hours", minutes, "minutes")
    
sec = 71
convert(sec)
