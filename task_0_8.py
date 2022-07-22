def convert(number):
    hour = number // 60
    number %= 60 
    minutes = number 
    if(hour==0 and minutes==1):
        return f"{hour} hour,{minutes} minute"
    elif(hour==1 and minutes==0):
        return f'{hour} hour, {minutes} minutes'
    elif (hour==0 and minutes>1):
        return f'{hour} hour, {minutes} minutes'
    elif(hour==1 and minutes>1):
        return f"{hour} hour, {minutes} minutes"
    elif(hour>1 and minutes ==1):
        return f"{hour} hours, {minutes} minute"
    elif (hour==1 and hour==1):
        return f'{hour} hour, {minutes} minute'
    else:    
        return f"{hour} hours, {minutes} minutes"
         
print(convert(71))
