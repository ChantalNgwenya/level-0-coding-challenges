
def convert(sec):
    # 1 hour = 60 min

    hour = sec // 60
    sec %= 60
    # 1 min = 60 sec
    minutes = sec 
    if (hour==1 and minutes==1):
        print(hour, "hour", minutes, "minute")
    elif(hour==1 and minutes>1):
        print(hour, "hour", minutes, "minutes")
    elif(hour >1 and minutes ==1):
        print(hour, "hours", minutes, "minute")
    else:
    print(hour, "hour/s", minutes, "minute/s")
    
sec = int(input("Enter the number: "))
convert(sec)
